T = int(input())
code = {"0001101":0, "0011001":1, "0010011":2, "0111101":3, "0100011":4, "0110001":5, "0101111":6, "0111011":7, "0110111":8, "0001011":9}

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    pwd =  [input().strip() for _ in range(N)]

    numbers = None
    for line in pwd:
        if '1' in line:
            # 암호코드의 마지막 1 찾기
            end = line.rfind('1')
            start = end - 56 + 1
            real_code = line[start:end + 1]

            # 암호코드 숫자 디코딩
            numbers = [code[real_code[i:i + 7]] for i in range(0, 56, 7)]
            break

    if numbers:
        odd_sum = sum(numbers[i] for i in range(0, 8, 2))
        even_sum = sum(numbers[i] for i in range(1, 8, 2))
        total_sum = odd_sum * 3 + even_sum

        if total_sum % 10 == 0:
            result = sum(numbers)
        else:
            result = 0
    else:
        result = 0

    print(f"#{test_case} {result}")
