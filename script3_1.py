f = open('input.txt', 'r')
a,b=map(int,f.readline().split())
c=f.readline()
t=open('output.txt', 'w')
if c=='-\n':
    print(a-b)
if c=='+\n':
    print(a+b)
if c=='*\n':
    print(a*b)
