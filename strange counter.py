"""
t=int(input())
r=1
for i in range(100):
    x=(3 * (2 ** i)) + r
    if t>=r and t<x:
        print(x-t)
        break
    else:
        r=x

import math
t=int(input())
while t:
    t-=1
    l=[]
    x,k=map(int,input().split())
    while x % 2 == 0:
        l.append(2)
        x = x / 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            l.append(int(i))
            x = x / i
    if x > 2:
        l.append(int(x))
"""
import math
t=int(input())
while t:
    t-=1
    c=0
    x,k=map(int,input().split())
    while x % 2 == 0:
        c+=1
        x = x / 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            c+=1
            x = x / i
    if x > 2:
        c+=1
    if c>=k:
        print(1)
    else:
        print(0)