n=int(input())
def f(n):
    a=0
    b=1
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        for i in range(n-2):
            a, b=b, a+b
        return b
print(f(n))