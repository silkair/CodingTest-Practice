def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N:
        return 0
    if grid[x][y]==0:
        return 0
    
    grid[x][y] = 0
    count = 1
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        count += dfs(nx,ny)
        
    return count

dx=[-1,1,0,0]
dy=[0,0,-1,1]

N = int(input())
grid = [list(map(int,input().strip())) for _ in range(N)]

results = []

for i in range(N):
    for j in range(N):
        if grid[i][j]==1:
            result=dfs(i,j)
            results.append(result)
            
results.sort()
print(len(results))
for size in results:
    print(size)