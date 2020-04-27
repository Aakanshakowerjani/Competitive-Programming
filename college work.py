"""
l=list(map(str,input().split(',')))
l.sort()
for i in l:
    print(i,end=",")


l=list(map(str,input().split()))
s=list(set(l))
s.sort()
print(*s)

n=int(input('enter an integer value'))
while n>=0:
    print(n)
    n-=1

##palindrome
n=int(input('enter an interger'))
r=0
x=n
while n>0:
    a=n%10
    r=r*10+a
    n//=10
if r==x:
    print("no is palindrome")
else:
    print("no is not plaindrome")

##Armstrong
n=int(input("enter integer"))
s=0
c=0
x=y=n
while n>0:
    n//=10
    c+=1
while x>0:
    a=x%10
    s+=a**c
    x//=10
if s==y:
    print("armstong")
else:
    print("not armstrong")

##Prime
n=int(input("enter integer"))
c=0
for i in range(2,n):
    if n%i==0:
        c=1
        break
if c==1:
    print("not prime")
else:
    print("prime")

a=8
print(type(a))
b=10.8
print(type(b))
c='hello'
print(type(c))
d=[1,'hi',40.5]
print(type(d))
e=(11,'hi',20.5)
print(type(e))
f={8:'hi','hello':89}
print(type(f))
g={7,9,8}
print(type(g))

d={1:'hi','hello':10.4,5:'yes',6:9}
print(d)
print(d.keys())
print(d.values())
print(d.pop(6))
print(d)

import math
print(1000*((10/2)**(2*4)))
print(math.sqrt((5-3)**2 + (8-5)**2))

s=input()
s1=input()
s1=set(s1)
c=0
for i in set(s):
    if i in s1:
        c+=1
print(c)
"""
l=list(map(str,input().split()))
s=list(set(l))
s.sort()
for i in s:
    print(i,l.count(i),end=' ')