from collections import deque
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for neighbors in graph:
    neighbors.sort()

visited_dfs = [False] * (N + 1)
dfs(graph, V, visited_dfs)
print()
bfs(graph, V)
