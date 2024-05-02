visited = set()
node = "A"
graph = {'A':['B','C','D'],
         'B':['A','E','D'],
         'C':['A','D'],
         'D':['A','B','C','E'],
         'E':['B','D']}

def DFS(node,visited,graph):
    if node not in graph:
        print("Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


DFS('A',visited,graph)



