p=input().split()
m=[]
for i in range(0,len(p)-1,2):
    m.append(int(p[i+1]))
    m.append(int(p[i]))
if len(p)%2!=0:
    m.apppend(int(p[len(p)-1]))
print(m)