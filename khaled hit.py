t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    size=int(n/4)
    l.sort()
    print(l)
    c=0
    final=[]
    for i in l[1::size]:
        #print(i)
        if i+1<len(l):
            if i == i+1:
                c=1
                break
            else:
                final.append(i+1)
    print(final)
    if c==0:
        for i in final:
            print(i,end=' ')
    else:
        print(-1)