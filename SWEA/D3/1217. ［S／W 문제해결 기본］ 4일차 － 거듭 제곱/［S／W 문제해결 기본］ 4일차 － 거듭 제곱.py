def mul(N, M):
    if M == 0:
        return 1
    else:
        return N*mul(N,M-1)


for test_case in range(10):
    T = int(input())
    N, M = map(int, input().split())

    result = mul(N,M)

    print(f"#{T} {result}")