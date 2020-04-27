"""
t=int(input())
while t:
    t-=1
    n,k,p=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    s=sum(l1)+sum(l2)
    for i in range(2*k-p):
        if l1[-1]>l2[-1]:
            s-=l2[-1]
            l2.pop()
        else:
            s-=l1[-1]
            l1.pop()
    print(s)

l1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print(l1)
for i in range(4):
    l=list(map(int,input().split()))
    m=0
    for j in range(len(l)):
        l1[j][m]+=l[j]
        m+=1
        print(l1)
print(l1)
"""
t=int(input())
while t:
    t-=1
    l=[]
    s=0
    n,k,p=map(int,input().split())
    for i in range(n):
        l1=list(map(int,input().split()))
        l.append(l1)
        s+=sum(l1)
    x=k*n-p
    while x>0:
        m=0
        ind=0
        s1=0
        for i in range(len(l)):
            print(l[i])
            s1+=l[i][-1]
            if l[i][-1]>m:
                m=l[i][-1]
                ind=i
        for i in range(len(l)):
            if i!=ind:
                l[i].pop()
        s-=s1-m
        x-=1
    print(s)
