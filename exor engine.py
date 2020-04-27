
#DONE IN CPP#

"""
a=[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
t=int(input())
while t:
    t-=1
    n,q=map(int,input().split())
    l=list(map(int,input().split()))
    p=[]
    for i in range(q):
        p=int(input())
        c1=0
        c2=0
        for i in l:
            b=0
            x=p^i
            while x>0:
                b+=a[x & 0xf]
                x=x>>4
            if b%2==0:
                c1+=1
            else:
                c2+=1
        print(c1,end=' ')
        print(c2)

print(7^2)
print(bin(7^2))
print(7^6)
print(bin(7^6))
print(9^4)
print(bin(9^4))
print(3^8)
print(bin(3^8))
print(bin(3))
print(bin(7))
print(bin(9))

print(7^3)
print(bin(7^3))
print(7^9)
print(bin(7^9))
print(9^5)
print(bin(9^5))
print(5^9)
print(bin(5^9))

print(8^2)
print(bin(8^2))
print(6^4)
print(bin(6^4))
print(8^6)
print(bin(8^6))
print(10^4)
print(bin(10^4))


print(8^3)
print(bin(8^3))
print(6^9)
print(bin(6^9))
print(2^3)
print(bin(2^3))
print(10^11)
print(bin(10^11))

print(bin(31))
print(8>>4)
print(5>>4)
print(31>>4)
print(bin(2))
print(bin(10))

print('change')
n=100
while n>0:
    print(bin(n))
    n-=1
a=[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
def func(x):
    n=0
    if x==0:
        return a[0]
    n=x & 0xf
    return a[n]+func(x>>4)
print(func(99903392))

b=0
x=99903392
while x>0:
    b+=a[x & 0xf]
    x=x>>4
print(b)
print(100000^100000000)
print(bin(100000^100000000))


print(100000^100000000)

l=[]
for i in range(1,99903393):
    l.append(bin(i))
print(l)

print(3^4)
print(bin(3^4))

W=int(input())
H=int(input())
W1=int(input())
H1=int(input())
C=0
while W>W1:
    C+=1
    if W%2==0:
        W=W//2
    else:
        W=(W+1)//2
while H>H1:
    C+=1
    if H%2==0:
        H=H//2
    else:
        H=(H+1)//2

print(C)

t=int(input())
while t:
    t-=1
    n,q=map(int,input().split())
    l=list(map(int,input().split()))
    c1=0
    c2=0
    for i in l:
        if i%2==0:
            c1+=1
        else:
            c2+=1
    for i in range(q):
        p=int(input())
        if p%2==0:
            print(c1,end=' ')
            print(c2)
        else:
            print(c2,end=' ')
            print(c1)


print(7)
print(bin(7))
print(7^8)
print(bin(7^8))
print(7^2)
print(bin(7^2))
print(7^10)
print(bin(7^10))
print(7^5)
print(bin(7^5))
print(7^3)
print(bin(7^3))
print(7^9)
print(bin(7^9))





print(3)
print(bin(3))
print(3^5)
print(bin(3^5))
print(3^4)
print(bin(3^4))

print(15)
print(bin(15))
print(15^7)
print(bin(15^7))
print(15^8)
print(bin(15^8))

print(bin(15))
print(bin(8))

print(bin(7))




for i in range(50):
    if i%2!=0:
        print(i)
        print(bin(i))

"""
print('o e')
print(bin(1))
print(bin(3))
print(bin(1^3))

print('e e')
print(bin(3))
print(bin(5))
print(bin(3^5))

print('o o')
print(bin(1))
print(bin(7))
print(bin(1^7))

print('e o')
print(bin(5))
print(bin(7))
print(bin(5^7))

print(bin(10))
print(bin(5^10))