p=input().split()
for i in range(0, len(p)):
    if p.count(p[i])==1:
        print(p[i])