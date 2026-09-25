n=[int(x) for x in input().split()]
h=1
for i in n:
    h*=int(i)
print(h**(1/len(n)))

