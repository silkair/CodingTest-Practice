T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    snail = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, go = 0, 0 , 0
    num = 1

    for _ in range(N*N):
        snail[x][y] = num
        num += 1

        nx, ny = x+dx[go], y+dy[go]

        if not (0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0):
            go = (go+1)%4
            nx, ny = x + dx[go], y+dy[go]

        x, y = nx, ny

    print(f"#{test_case}")
    for row in snail:
        print(" ".join(map(str, row)))
