t=int(input())
while t:
    t-=1
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    l=l[::-1]
    for i in l:
        if i<=d:
            d=d-(d%i)
    print(d)