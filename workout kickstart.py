t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    for i in range(len(l)-1):
        l1.append(abs(l[i]-l[i+1]))
    while k>0:
        if max(l1)%2==0:
            a=max(l1)/2
            l1.append(a)
            l1.append(a)
        else:
            a=int(max(l1)/2)
            b=int(max(l1)/2)+1
            l1.append(a)
            l1.append(b)
        l1.remove(max(l1))
        k-=1
    print(int(max(l1)))

