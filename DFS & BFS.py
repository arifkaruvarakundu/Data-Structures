#---------- DFS -------------#

def dfs(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend([v for v in graph[vertex] if v not in visited])

    return visited

#------------------ BFS ---------------------------#
 
def bfs(graph,start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])

    return visited


    


