import math
def digitsum(n):
    s=0
    while n:
        s+=(n%10)
        n//=10
    return s
def chckprime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
n=int(input())
c=0
for i in range(n+1):
    if chckprime(digitsum(i)*2):
        c+=1
        print(i,i)
for i in range(n):
    for j in range(i+1,n+1):
        if chckprime(digitsum(i)+digitsum(j)):
            c+=1
            print(i,j)
print(c)