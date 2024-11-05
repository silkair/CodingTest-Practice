N, M = map(int,input().split())
arr = []

for i in range(N) :
    arr.append(i+1)

for j in range(M) :
    a, b = map(int,input().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

for i in range(N):
    print(arr[i], end=' ')