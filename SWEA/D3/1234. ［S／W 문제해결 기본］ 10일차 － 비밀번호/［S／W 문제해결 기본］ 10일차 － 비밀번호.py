for test_case in range(1, 11):
    n, pw = input().split()
    pw = list(pw)

    for _ in range(len(pw)):
        result = []
        i = 0
        while i < len(pw):
            if i < len(pw) - 1 and pw[i] == pw[i + 1]:
                i += 2
            else:
                result.append(pw[i])
                i += 1
        if len(result) == len(pw):
            break
        pw = result
    print(f"#{test_case} {''.join(pw)}")