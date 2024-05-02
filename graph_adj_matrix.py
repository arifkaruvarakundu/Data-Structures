class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        # Assuming the graph is undirected; for a directed graph, you may set only one of these
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def display(self):
        for row in self.adj_matrix:
            print(row)

if __name__ == "__main__":
    # Create a graph with 5 vertices
    my_graph = Graph(5)

    # Add edges to the graph
    my_graph.add_edge(0, 1)
    my_graph.add_edge(0, 4)
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 4)

    # Display the adjacency matrix
    print("Adjacency Matrix:")
    my_graph.display()
