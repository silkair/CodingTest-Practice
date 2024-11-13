T = int(input())
dict_month = {'1' : 31, '2' : 28, '3' : 31, '4' : 30, '5' : 31, '6' : 30, '7' : 31, '8' : 31, '9' : 30, '10' : 31, '11' : 30, '12' : 31}

for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    result = 0

    if a==c:
        result = d - b + 1
    else :
        for month in range (a,c) :
             result += dict_month[str(month)]
        result += d - b + 1
    print(f"#{test_case} {result}")
