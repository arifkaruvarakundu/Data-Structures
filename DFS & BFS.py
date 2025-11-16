#---------- DFS -------------#

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend([v for v in graph[vertex] if v not in visited])
    return visited
    
#------------------ BFS ---------------------------#
 
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            for v in graph[vertex]:
                if v not in visited and v not in queue:
                    queue.append(v)
    return visited


    


