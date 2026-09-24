p=input().split()
m=0
k=0
for i in range(0, len(p)):
    if m<p.count(p[i]):
        k=p[i]
    m=max(m,p.count(p[i]))
print(k)