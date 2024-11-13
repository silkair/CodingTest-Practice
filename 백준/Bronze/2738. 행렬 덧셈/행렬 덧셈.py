N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))

for j in range(N):
    B.append(list(map(int, input().split())))

for k in range(N):
    for l in range(M):
        print(A[k][l] + B[k][l], end=" ")
    print()

