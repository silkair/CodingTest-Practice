from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maze, N, M):
    queue = deque([(0,0)])
    maze[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x==N-1 and y==M-1:
            return maze[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<N and 0 <=ny<M and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
                    
    return -1  

N, M = map(int,input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

print(bfs(maze, N, M))