from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex,neibours in self.graph.items():
            print(f"Vertex{vertex}:{neibours}")

my_graph = Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 4)
my_graph.add_edge(4, 2)

my_graph.display()