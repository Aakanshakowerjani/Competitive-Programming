"""
from itertools import combinations
n=int(input())
s=input()
s1=s
st=list(set(s))
comb=combinations(st,len(st)-2)
for i in comb:
    s1=s

# Python Program to find LCM of n elements

def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


l = [2, 7, 3, 9, 4,7]

num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)

for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])

print(lcm)

# Code contributed by Mohit Gupta_OMG



t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    x=1
    while m>=1:
        if m not in l:
            x=m
            break
        else:
            m-=1
    print(x)

    """
t=int(input())
while t:
    t-=1
    t = int(input())
    while t:
        t -= 1
        n, m = map(int, input().split())
        l = list(map(int, input().split()))
        x = 1
        while m >= 1:
            if m not in l:
                x = m
                break
            else:
                m -= 1t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    x=1
    while m>=1:
        if m not in l:
            x=m
            break
        else:
            m-=1
    print(x)t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    x=1
    while m>=1:
        if m not in l:
            x=m
            break
        else:
            m-=1
    print(x)
        print(x)