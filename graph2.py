import networkx as nx
import matplotlib.pyplot as plt   
import json
from collections import defaultdict

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


# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, lvl):
    explored = []
    level = [None] * (max(graph) + 1)
      
    # Queue for traversing the 
    # graph in the BFS
    queue = [[start]]
    level[start] = 0
      
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        # Codition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
            
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                level[neighbour] = level[node] + 1
        
            explored.append(node)
            print(level[node])
                
    return explored





target = input('target')
target = int(target)
levels = input('level')
levels = int(levels)

if __name__ == "__main__":
    graph = build_graph(all_nodes)
      
    print(BFS_SP(graph, target, levels))

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

