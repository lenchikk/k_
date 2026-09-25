a, b=map(int, input().split())
def f(a,b):
    if a>b:
        while b!=0:
            a, b=b, a%b
        return a
    elif a<b:
        while a!=0:
            b ,a=a, b%a
        return b
    else:
        return a
d=f(a,b)
m=100000000000000000000000000
X=100000000000000000000000000
Y=0
if a>b:
    for x in range (-a,a):
        for y in range (-a, a):
            if x*a+y*b==d:
                if abs(x)+abs(y)<m:
                    m=abs(x)+abs(y)
                    X=x
                    Y=y
                if abs(x)+abs(y)==m:
                    if x<X:
                        X = x
                        Y = y
                break
else:
    for x in range (-b,b):
        for y in range (-b, b):
            if x*a+y*b==d:
                if abs(x)+abs(y)<m:
                    m=abs(x)+abs(y)
                    X=x
                    Y=y
                if abs(x)+abs(y)==m:
                    if x<X:
                        X = x
                        Y = y
                break
print(X, Y, d)