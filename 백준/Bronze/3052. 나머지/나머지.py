arr = [0]*42
answer = 0

for i in range(10):
    n = int(input())
    k = n%42
    if arr[k] == 0:
        arr[k] = 1
        answer = answer + 1
    else:
        continue
print(answer)