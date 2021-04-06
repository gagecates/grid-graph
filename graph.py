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

# add edges to empty list
edges = []

for i in data['lines']:
    if i['i'] and i['j'] in nodes:
        edges.append((i['i'],i['j']))

# for transformers add edges according to value of k
for i in data['transformers']:
    if i['k'] != 0:
        if i['i'] and i['j'] in nodes:
            edges.append((i['i'],i['j']))
        elif i['j'] and i['k'] in nodes:
            edges.append((i['j'],i['k']))
        elif i['k'] and i['i'] in nodes:
            edges.append((i['k'],i['i']))
    else:
        if i['i'] and i['j'] in nodes:
            edges.append((i['i'],i['j']))

first_edge = edges[0]
last_vertex = nodes[len(nodes) - 1]
print(edges[10],edges[11],edges[12])


# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s, lvl):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # track levels from root node
        level = [None] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # list of final nodes returned
        final_nodes = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        level[s] = 0

        # while still unvisited nodes
        while queue:
            # break and return nodes once user input level reached
            if level[s] == lvl +1:
                break
            else:
                print(level[s])
                # Dequeue a vertex from
                # queue and print it
                s = queue.pop(0)
                final_nodes.append(s)
                print (s, end = " ")

                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
                        level[i] = level[s] + 1

        return final_nodes

# create graph above
g = Graph()

# add all edges to the adjacency list
for i in edges:
    g.addEdge(i[0],i[1])


# print(g.BFS(10007, 2))
target = input('target')
target = int(target)
levels = input('level')
levels = int(levels)

user_requested_nodes = (g.BFS(target, levels))




'''
# initialize empty directed graph and convert to undirected
DG = nx.DiGraph()
G = nx.Graph(DG)

# add nodes and edges to graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
#plt.show()

jsonfile.close()
'''
