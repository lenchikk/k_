n=int(input())
p=input()
k=''
m=[]
for i in range(0, len(p)-1, n):
    for j in range(n):
        m.append(p[i+j])
    m=m[::-1]
    for u in m:
        k+=u
    print(m)
    m=[]
print(k)

