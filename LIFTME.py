t=int(input())
while t:
    t-=1
    x=0
    c=0
    n,q=map(int,input().split())
    for i in range(q):
        a,b=map(int,input().split())
        c+=abs(x-a)
        x=a
        c+=abs(x-b)
        x=b
    print(c)

print(137438953472 % ((10**9)+7))