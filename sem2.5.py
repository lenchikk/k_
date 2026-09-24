p=input().split()
a=p.pop(len(p)-1)
p.insert(0,a)
print(''.join(p))