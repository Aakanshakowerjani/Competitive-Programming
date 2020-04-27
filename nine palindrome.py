"""
def pal(n):
    x=n
    r=0
    while x>0:
        r=r*10+(x%10)
        x//=10
    return r==n
t=int(input())
while t:
    t-=1
    n=int(input())
    for i in range(1,100001):
        if pal(i) and i%9==0:
            print(i)


import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x
def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
"""
import math
t=int(input())
while t:
    t-=1
    x,y=map(int,input().split())
    if x==y!=1:
        print('NO')
    elif abs(x-y)==1:
        print('YES')
    else:
        x1 = 5 * x * x + 4
        x2 = 5 * x * x - 4
        s1 = int(math.sqrt(x1))
        s2 = int(math.sqrt(x2))
        if s1 * s1 == x1 or s2 * s2 == x2:
            f1=1
        else:
            f1=0
        y1 = 5 * y * y + 4
        y2 = 5 * y * y - 4
        s11 = int(math.sqrt(y1))
        s22 = int(math.sqrt(y2))
        if s11 * s11 == y1 or s22 * s22 == y2:
            f2=1
        else:
            f2=0
        if f1==f2==1:
            print('YES')
        else:
            print('NO')