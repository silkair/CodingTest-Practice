for test_case in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    block = 0

    for i in range(n):
        sth = False
        for j in range(n):
            if table[j][i] == 1:
                sth = True
            elif table[j][i] == 2:
                if sth==True:
                    block += 1
                    sth=False
            else:
                continue
    print(f"#{test_case} {block}")