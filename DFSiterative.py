node = "A"
graph = {'A':['B','C','D'],
         'B':['A','E','D'],
         'C':['A','D'],
         'D':['A','B','C','E'],
         'E':['B','D']}

def DFSiterative(node,graph):
    visited = set()
    if node not in graph:
        print("Node is not present in the graph")
        return

    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

    

DFSiterative("B",graph)
