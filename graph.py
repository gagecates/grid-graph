import networkx as nx
import matplotlib.pyplot as plt   
import json

# open json file
jsonfile = open('sample_data.json')

# parse json and return python dictionary
data = json.load(jsonfile)

# add nodes to empty list
nodes = []

for i in data['buses']:
    nodes.append(i['number'])

# print(nodes)

# add edges to empty list
edges = []

for i in data['lines']:
    edges.append((i['i'],i['j']))

# print(len(edges))


# initialize empty graph
G = nx.DiGraph()

# add nodes and edges to graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()

jsonfile.close()
