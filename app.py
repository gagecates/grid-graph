import os
import networkx as nx
import matplotlib.pyplot as plt  
import matplotlib 
import json
from collections import defaultdict
import queue 
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin

# creates non interactive backend for GUI to avoid app crash
#matplotlib.use('agg')


# open json file
jsonfile = open('sample_data.json')

# parse json and return python dictionary
data = json.load(jsonfile)


# find nodes --------------------------------------------
def findNodes():
# add nodes to empty list
    nodes = []

    for i in data['buses']:
        nodes.append(i['number'])

    return nodes

# find edges -------------------------------------------
def findEdges(nodes):
    edges = []

    for i in data['lines']:
        line = [i['i'], i['j']]
        exists =  all(elem in nodes for elem in line)
        if exists:
            edges.append((i['i'],i['j']))
    
    for i in data['transformers']:
        if i['k'] != 0:

            line1 = [i['i'], i['j']]
            exists1 =  all(elem in nodes for elem in line1)
            if exists1:
                edges.append((i['i'],i['j']))

            line2 = [i['j'], i['k']]
            exists2 =  all(elem in nodes for elem in line2)
            if exists2:
                edges.append((i['j'],i['k']))

            line3 = [i['k'], i['i']]
            exists3 =  all(elem in nodes for elem in line3)
            if exists3:
                edges.append((i['k'],i['i']))

        else:
            line1 = [i['i'], i['j']]
            exists1 =  all(elem in nodes for elem in line1)
            if exists1:
                edges.append((i['i'],i['j']))

    return edges

# BFS algorithm to find target nodes --------------------------
# each node starting from x using BFS 
def getTargetNodes(graph, x, lvl):
    
    # array to store level of each node 
    level = [None] * (max(graph) + 1)
    marked = [False] * (max(graph) + 1) 
    explored = []

    # create a queue 
    que = queue.Queue()

    # enqueue element x 
    que.put(x) 

    # initialize level of source 
    # node to 0 
    level[x] = -1

    # marked it as visited 
    marked[x] = True

    # do until queue is empty 
    while (not que.empty()):

        # get the first element of queue 
        x = que.get()

        # traverse neighbors of node x
        for i in range(len(graph[x])):
            
            # b is neighbor of node x 
            b = graph[x][i] 

            # if b is not marked already 
            if (not marked[b]): 
                # level of b is level of x + 1 
                level[b] = level[x] + 1
                print(level[b])
                
                if level[b] == lvl + 1:
                    return explored[:-1]
                else:
                    # enqueue b in queue 
                    que.put(b)
                    # mark b 
                    marked[b] = True

        explored.append(x)

    return explored

# construct graph --------------------------------
def build_graph():
    all_nodes = findNodes()
    all_edges = findEdges(all_nodes)
    graph = defaultdict(list)
    
    # Loop to iterate over every 
    # edge of the graph
    for edge in all_edges:
        a, b = edge[0], edge[1]
        
        # Creating the graph 
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph

def display_graph(edges):
    # graph display output ------------------------------
    # initialize empty directed graph and convert to undirected
    DG = nx.DiGraph()
    G = nx.Graph(DG)

    # add nodes and edges to graph
    # G.add_nodes_from(user_req_nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    matplotlib.pyplot.switch_backend('Agg')

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G, pos, font_size=6)
    #plt.show()
   
    client_image_file = '../plot.png'
    plt.savefig('./front-end/build/plot.png', dpi=1000)
    
    return client_image_file


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder='./front-end/build', static_url_path='/')


    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true',)
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add(
            'Access-Control-Allow-Origin',
            '*')
        return response


    @app.route('/')
    def index():
        return app.send_static_file('index.html')


    @app.route('/graph', methods=["POST"])
    def build_user_graph():
        graph_data = request.get_json()
        target = int(graph_data['target'])
        levels = int(graph_data['levels'])

        graph = build_graph()
        #print(graph[10001])
        
        user_req_nodes = getTargetNodes(graph, target, levels)
        user_req_edges = findEdges(user_req_nodes)
        #print(user_req_edges)
        #print(user_req_nodes)
        image_file = display_graph(user_req_edges)
        
        if len(user_req_edges) == 0:
            return jsonify({
                'message': 'There are no other buses connected to this bus. Please enter a new starting point.',
                'image': None
            })
        else:

            return jsonify({
                'message': 'success',
                'image': image_file
            })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()


