a,b = map(int,input().split())
c = int(input())

fin = int(b)+int(c)

if fin >= 60:
  a += int(fin // 60)
  fin = int(fin % 60)
  if a >= 24:
    a -= 24

print(a,fin)