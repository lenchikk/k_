a=[[0]*5]*5
print(a)
print([id(r) for r in a])
a[0][0]=5
print(a)