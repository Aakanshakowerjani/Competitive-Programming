t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    m=0
    for i in l:
        if m<l.count(i):
            m=l.count(i)
    print(len(l)-m)