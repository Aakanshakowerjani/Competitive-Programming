
from itertools import combinations_with_replacement
def digit_sum(n):
    s=0
    while n>0:
        a=n%10
        s+=a
        n//=10
    return s
def prime(n):
    if n==1 or n==0:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
n=int(input())
l=[]
for i in range(n+1):
    l.append(i)
comb=combinations_with_replacement(l,2)
l1=[]
c=0
for i in comb:
    print(i)
    if prime(digit_sum(i[0])+digit_sum(i[1])):
        c+=1
        l1.append([digit_sum(i[0]),digit_sum(i[1])])
print(c)
print(l1)
"""
def solve(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    return ('YES' if n==sum(l) else 'NO')
t=int(input())
for _ in range(t):
    n=int(input())
    out_=solve(n)
    print(out_)
"""