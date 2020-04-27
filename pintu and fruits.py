t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=[-1]*m
    st=set(l1)
    for i in st:
        l3[i-1]+=1
    for i in range(n):
        l3[l1[i]-1]+=l2[i]
    l4=[]
    for i in l3:
        if i!=-1:
            l4.append(i)
    if len(l4)==0:
        print(0)
    else:
        print(min(l4))