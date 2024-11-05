n = int(input())
L = list(map(int,input().split()))
max = float('-inf')  # 가장 작은 수
min = float('inf')   # 가장 큰 수

for i in range(n) :
    if L[i]>max:
        max = L[i]
    if L[i]<min :
        min = L[i]
        
print(min, max)