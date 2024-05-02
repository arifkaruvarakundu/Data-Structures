
start = "A"
graph = {'A':['B','C','D'],
         'B':['A','E','D'],
         'C':['A','D'],
         'D':['A','B','C','E'],
         'E':['B','D']}

def bfs(graph,start):
    visited = set()
    queue = []
    queue.append(start)

    while queue:
        current = queue.pop(0)

        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                queue.append(i)

    

bfs(graph,"E")


