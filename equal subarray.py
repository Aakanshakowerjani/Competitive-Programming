n=int(input())
k=int(input())
l=list(map(int,input().split()))
c=0
x=n-1
while x>1:
    for i in range(0,n+1-x):
        m=max(l[i:i+x])
        sm=0
        for i in l[i:i+x]:
            sm+=m-i
        if sm<=k:
            c=1
    if c==1:
        print(x)
        break
    else:
        x-=1

"""
    x=list(combinations(l,n-1))
    for i in x:
        m=max(i)
        sm=0
        for j in i:
            sm+=(m-j)
        if sm<=k:
            c=1
    if c==1:
        print(n-1)
        break
    else:
        n-=1



l=[1,2,4,5,6,4,7,93,2,2,5,4,5,22,1,4,45,5,52,2,111]
for i in range(0,len(l)+1-3):
    print(sum(l[i:i+3]))
"""