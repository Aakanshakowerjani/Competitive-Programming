"""
def func(l):
    if len(l)==1:
        return l[0]
    else:
        n1=int(l)
        a = n1 % 10
        n1 //= 10
        l1 = []
        while n1 > 0:
            b = n1 % 10
            l1.append(abs(b - a))
            n1 //= 10
            a = b
        return func(l1)
n=int(input())
n1=int(input())
a=n1%10
n1//=10
l=[]
while n1>0:
    b=n1%10
    l.append(abs(b-a))
    n1//=10
    a=b
print(func(l))
"""
def func(l):
    if len(l)==1:
        return l[0]
    else:
        l1=[]
        for i in range(len(l)-1):
            l1.append(abs(l[i]-l[i+1]))
        return func(l1)
n=int(input())
n1=int(input())
l=[]
while n1>0:
    l.append(n1%10)
    n1//=10
print(func(l[::-1]))