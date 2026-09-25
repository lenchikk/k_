n, s=map(str, input().split())
n=int(n)
for i in range (1,(n//2)+2):
    print(s*i)
for i in range ((n//2)+2, 1, -1):
    print(s*i)