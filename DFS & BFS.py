#---------- DFS -------------#

def dfs(graph,start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)

    return visited

#------------------ BFS ---------------------------#
 
def bfs(graph,start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                queue.append(i)

    return visited


    


