# cook your dish here
t=int(input())
while t:
    t-=1
    l=[]
    st=set()
    l1=[]
    l2=[]
    n,k=map(int,input().split())
    for i in range(k):
        l=list(map(int,input().split()))
        l1.append(l[0])
        if l[1] not in l1 and l[1] not in l2:
            l2.append(l[1])
        else:
            l2.append(0)
    st=set(l1)
    print(len(st))
    if len(st)==n:
        lst=[0]*n
        print(*l1)
    else:
        print(*l2)