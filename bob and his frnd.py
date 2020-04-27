t=int(input())
while t:
    t-=1
    n,a,b,c=map(int,input().split())
    l=list(map(int,input().split()))
    m=abs(b-l[0])+abs(a-l[0])
    for i in l:
        if m>abs(b-i)+abs(a-i):
            m=abs(b-i)+abs(a-i)
    print(m+c)