"""
from itertools import combinations
t=int(input())
while t:
    t-=1
    n,b=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    while n>=0:
        comb=combinations(l,n)
        s=0
        for i in comb:
            if sum(i)>s and sum(i)<=b:
                s=sum(i)
                l1.append(n)

        n-=1
    if len(l1)==0:
        print(0)
    else:
        print(max(l1))
"""


def maxi(l, n, b):
    c = 0
    s = 0
    l.sort(reverse=False)
    for i in range(0, n, 1):
        if (s + l[i] <= b):
            s = s + l[i]
            c += 1
    return c
t=int(input())
while t:
    t-=1
    n,b=map(int,input().split())
    l=list(map(int,input().split()))
    print('Case #',end='')
    print(t,end='')
    print(':',end=' ')
    print(maxi(l, n, b))

