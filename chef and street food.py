t=int(input())
while t:
    t-=1
    n=int(input())
    pro=0
    for i in range(n):
        s,v,p=map(int,input().split())
        x=int(p / (s + 1))
        if pro<x*v:
            pro=x*v
    print(pro)
