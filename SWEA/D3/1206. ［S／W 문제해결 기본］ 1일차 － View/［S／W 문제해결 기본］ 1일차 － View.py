for test_case in range(1, 11):
    N = int(input())

    bd = list(map(int,input().split()))
    answer = 0

    for i in range(2,N-1):
        if bd[i]>bd[i-2] and bd[i]>bd[i-1] and bd[i]>bd[i+2] and bd[i]>bd[i+1]:
            answer = answer + min(bd[i]-bd[i-2], bd[i]-bd[i-1], bd[i]-bd[i+2],bd[i]-bd[i+1])

    print(f"#{test_case} {answer}")
