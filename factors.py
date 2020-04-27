def ispm(n1):
    if n1<=1:
        return False
    if n1<=3:
        return True
    if n1% 2 == 0 or n1 % 3 == 0:
        return False
    j = 5
    while j*j <= n1:
        if n1%j == 0 or n1% (j+2) == 0:
            return False
        j = j + 6
    return True
def fctr(number):
    value = 1
    c=0
    c1=0
    while (value <= number):
        if(number % value == 0):
            if ispm(value):
                c1+=1
            c+=1
        value = value + 1
    return c1,c

x=3
l=set()
for i in range(90000,100000):
   p,f=fctr(i)
   if p==x:
       l.add(f)
l=list(l)
l.sort()
print(l)
"""
def ispm(n1):
    if n1<=1:
        return False
    if n1<=3:
        return True
    if n1% 2 == 0 or n1 % 3 == 0:
        return False
    j = 5
    while j*j <= n1:
        if n1%j == 0 or n1% (j+2) == 0:
            return False
        j = j + 6
    return True
t=int(input())
while t:
    t-=1
    x,k=map(int,input().split())
    if k==0 :
        if x==1:
            print(1)
        else:
            print(0)
    elif k==1:
        print(1)
    else:
        if ispm(x):
            print(0)
        else:
            print(1)
        
    """