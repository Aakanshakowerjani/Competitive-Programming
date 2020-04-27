"""
t=int(input())
while t:
    t-=1
    n,a=map(int,input().split())
    y=a
    x=a
    z=3
    s=a
    for i in range(n-1):
       y=(x*y)%((10**9)+7)
       x=(y**z)%((10**9)+7)
       z+=2
       s+=(x%((10**9)+7))
    print(s)
    print(729*9)
for i in range(100):
    print(2**i,i)

    """
t=int(input())
while t:
    t-=1
    n,a=map(int,input().split())
    x=1
    y=1
    s=0
    for i in range(n):
        s+=(((a**x)%((10**9)+7))**y)%((10**9)+7)
        x=((x*y)%((10**9)+7))+(x%((10**9)+7))
        y+=2%((10**9)+7)
    print(s%((10**9)+7))
"""
print((10**9)+7)
print(1073741824 %((10**9)+7))
print((262**9)%((10**9)+7))
print(256**5)
"""
for i in range(100):
    print(2**i,i)
print(1099511627776%((10**9)+7))
