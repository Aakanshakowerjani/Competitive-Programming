"""
from itertools import combinations
l=[]
for i in range(0,9):
    a=int(input())
    l.append(a)
print(l)
x=()
comb=combinations(l,7)
c=0
for i in comb:
    c+=1
print(c)
for i in list(comb):
    if sum(i)==100:
        x=i
for i in x:
    print(i)

t=tuple(map(int,input().split()))
print(t)

from itertools import combinations
l=list(map(int,input().split()))
n=l[0]
m=l[1]
x=[]
li=[]
for i in range(1,n+1):
    li.append(i)
comb=combinations(li,2)
c=0
combi=[]
for i in comb:
    combi.append(i)
    c+=1
for i in range(m):
    x=tuple(map(int,input().split()))
    print(x)
    if x in combi:
        c-=1

"""
n=int(input())
m=int(input())
k=int(input())
l=[]
for i in range(m):
    x=int(input())
    a=x-k
    b=x+k
    for j in range(a,b+1):
        if j>0 and j<=n:
            l.append(j)
s=set(l)
c=0
print(s)
for i in s:
    c+=1
print(n-c)


