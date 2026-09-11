n=int(input())
m=[]
g=0
for i in range(n - 1):
    m.append(int(input()))
k=True
while k:
    k=False
    for g in range (n-2):
        for i in range(n-2-g):
            if m[i+1]<m[i]:
                m[i],m[i+1]=m[i+1],m[i]
                k=True
            g+=1
print(m)
j= list(range(1, n + 1))
print(j)
for i in range(len(m)):
    if m[i]!=j[i]:
        print(j[i])
        break