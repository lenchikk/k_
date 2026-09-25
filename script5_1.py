f = open('input.txt', 'r')
a,b=map(int,f.readline().split())
c=f.readline()
d=int(f.readline())
def f(N,l):
    k = 0
    n = 0
    while N > 0:
        n += (N % 10) * (l ** k)
        N = N // 10
        k += 1
    return n
def g(n,l):
    r=''
    while n > 0:
        r = str(n % l) + r
        n = n // l
    r=int(r)
    return r
A=f(a,d)
B=f(b,d)
if c=='-\n':
    print(g(A-B, d))
if c=='+\n':
    print(g(A+B, d))
if c=='*\n':
    print(g(A*B, d))