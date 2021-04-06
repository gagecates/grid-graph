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



# graph representation using adjacency list
class Graph:

    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to print a BFS of graph
    def BFS(self, s, lvl):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # track levels from root node
        #level = [None] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # list of final nodes returned
        final_nodes = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        level = 0

        # loop while still unvisited nodes
        while queue:
            print(level)
            if level >= lvl:
                break
            else:
                # Dequeue a vertex from
                # queue and print it
                s = queue.pop(0)
                final_nodes.append(s)
                
                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
                level += 1

        return final_nodes

# create graph above
g = Graph()

# add all edges to the adjacency list
all_edges = find_edges(all_nodes)
for i in all_edges:
    g.addEdge(i[0],i[1])


target = input('target')
target = int(target)
levels = input('level')
levels = int(levels)

user_req_nodes = (g.BFS(target, levels))
user_req_edges = find_edges(user_req_nodes)


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

