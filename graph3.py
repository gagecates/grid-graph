import networkx as nx
import matplotlib.pyplot as plt   
import json
from collections import defaultdict
import queue 

# open json file
jsonfile = open('sample_data.json')

# parse json and return python dictionary
data = json.load(jsonfile)

# add nodes to empty list
all_nodes = []

for i in data['buses']:
    all_nodes.append(i['number'])

# find edges from json file nodes
def find_edges(n):
    edges = []
    for i in data['lines']:
        if i['i'] and i['j'] in n:
            edges.append((i['i'],i['j']))

    # for transformers add edges taking into account value of k
    for i in data['transformers']:
        if i['k'] != 0:
            if i['i'] and i['j'] in n:
                edges.append((i['i'],i['j']))
            elif i['j'] and i['k'] in n:
                edges.append((i['j'],i['k']))
            elif i['k'] and i['i'] in n:
                edges.append((i['k'],i['i']))
        else:
            if i['i'] and i['j'] in n:
                edges.append((i['i'],i['j']))

    return edges


# function to determine level of 
# each node starting from x using BFS 
def printLevels(graph, x, lvl):
      
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
                
                if level[b] == lvl + 1:
                    if lvl == 1:
                        return explored[:-1]
                    else:
                        return explored
                else:
                    # enqueue b in queue 
                    que.put(b)
                    # mark b 
                    marked[b] = True

        explored.append(x)

    return explored[:-1]


# Function to build the graph
def build_graph(nodes):
    edges = find_edges(all_nodes)
    graph = defaultdict(list)
      
    # Loop to iterate over every 
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
          
        # Creating the graph 
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


target = input('target')
target = int(target)
levels = input('level')
levels = int(levels)

if __name__ == "__main__":
    graph = build_graph(all_nodes)
    
    print(graph[80005])
      
    print(printLevels(graph, target, levels))

#user_req_nodes = (g.BFS(target, levels))
#user_req_edges = find_edges(user_req_nodes)







'''
# initialize empty directed graph and convert to undirected
DG = nx.DiGraph()
G = nx.Graph(DG)

# add nodes and edges to graph
# G.add_nodes_from(user_req_nodes)
G.add_edges_from(user_req_edges)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()


jsonfile.close()
'''

