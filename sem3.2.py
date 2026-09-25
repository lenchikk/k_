n=int(input())
def f(n):
    a=[]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                while (n%i==0):
                    a.append(i)
                    n=n//i
        if len(a)==0:
            a.append(n)
        return a
print(f(n))