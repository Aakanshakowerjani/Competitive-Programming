t=int(input())
while t:
    t-=1
    n=int(input())
    s=0
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i]-i<=0:
            break
        else:
            s+=(l[i]-i)
    print(s%((10**9)+7))