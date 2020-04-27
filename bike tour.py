t=int(input())
x=1
while t:
    t-=1
    n,d=map(int,input().split())
    l=list(map(int,input().split()))
    l=l[::-1]
    for i in l:
        if i<=d:
            d=d-(d%i)
    print('Case #',end='')
    print(x,end='')
    print(':',d)
    x+=1