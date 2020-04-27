t=int(input())
while t:
    t-=1
    a,b,c=map(int,input().split())
    while True:
        if c<0:
            print(-1)
            break
        elif c%a==b:
            print(c)
            break
        else:
            c-=1