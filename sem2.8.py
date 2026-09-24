n=int(input())
p=list(map(int, input().split()))
for i in range(len(p)-1):
  for j in range(len(p)-i-1):
    if p[j] > p[j+1]:
      p[j], p[j+1] = p[j+1], p[j]
print(p[(n//2)])