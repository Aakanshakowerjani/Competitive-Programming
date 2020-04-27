"""
def func(s,sm):
    if len(s)==1:
        return sm
    elif min(s) == 0:
        if s[0]==0:
            return sm
        ind = s.index(min(s))
        sm += ind
        s = s[:ind]
        for i in range(len(s)):
            s[i] = s[i] - 1
        return func(s,sm)
    elif min(s) > 0:
        sm+=len(s)
        for i in range(len(s)):
            s[i] = s[i] - 1
        return func(s,sm)

t=int(input())
while t:
    t-=1
    n=int(input())
    sm=0
    s=list(map(int,input().split()))
    x=func(s,sm)
    print(x)
"""

t=int(input())
while t:
    t-=1
    n=int(input())
    sm=0
    s=list(map(int,input().split()))
    while True:
        if s[0]==0:
            break
        if 0 in s:
            ind=s.index(0)
            s=s[:ind]
        elif len(s) == 1:
            break
        else:
            sm+=len(s)
            s=[i-1 for i in s ]
    print(sm+s[0])








