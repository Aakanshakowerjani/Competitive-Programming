t=int(input())
while t:
    t-=1
    c,n=map(int,input().split())
    x=int(c/n)
    if x>n:
        sm=x+1
        for i in range(n-1):
            sm+=x
            x-=1
        print(c-sm)
    else:
        print(c)