import math

def ref(N, A, B):
    min_result = float('inf')
    sqrt_n = int(math.sqrt(N))

    for R in range(1, sqrt_n + 3):
        C=N//R
        cost = A*abs(R-C) + B*(N-R*C)
        min_result = min(min_result, cost)

        C_plus = C + 1
        if R * C_plus <= N:
            cost2 = A * abs(R - C_plus) + B * (N - R * C_plus)
            min_result = min(min_result, cost2)

        C_minus = C - 1
        if C_minus > 0 and R * C_minus <= N:
            cost3 = A * abs(R - C_minus) + B * (N - R * C_minus)
            min_result = min(min_result, cost3)

    return min_result

T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    result=ref(N, A, B)
    print(f"#{test_case} {result}")