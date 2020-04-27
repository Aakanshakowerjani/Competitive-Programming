t=int(input())
while t:
    t-=1
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    lst=[]
    for i in range(n-k,n+1):
        lst.append(i)
    x=n-(k+1)
    while x>0:
        lst.append(x)
        x-=1
    for i in lst:
        print(i,end=" ")
