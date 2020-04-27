"""
print(1^0)
print(1^1)
print(0^0)
print(0^1)
a='10010'
b='01110'
print(int(a) ^ int(b))

1
3
1110001101
1010101011
0000000011

def dTB(n):
    return bin(n).replace("b", "")

t=int(input())
while t:
    n=int(input())
    a=int(input(),2)
    for i in range(n):
        b=int(input(),2)
        a=a^b
    print(bin(a).count('1'))

t=int(input())
while t:
    n=int(input())
    for i in range(n-2):
        if i==0:
            a = int(input(), 2)
            print(a)
            b = int(input(), 2)
            print(b)
            a=a^b
        else:
            b = int(input(), 2)
            print(b)
            a=a^b
    print(bin(a).count('1'))
"""

t=int(input())
while t:
    t-=1
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    for i in range(len(l)):
        if i+1<len(l):
            if i==0:
                a=int(str(l[i]),2)
            else:
                a=l[i]
            b=int(str(l[i+1]),2)
            l[i+1]=a ^ b
    print(bin(l[-1]).count('1'))