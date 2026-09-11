N=int(input())
b=int(input())
c=int(input())
k=0
n=0
r=''
while N>0:
    n+=(N%10)*(b**k)
    N=N//10
    k+=1
while n>0:
    r=str(n%c)+r
    n=n//c
print(int(r))