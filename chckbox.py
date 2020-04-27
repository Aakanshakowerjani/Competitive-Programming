"""
t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    l1=[]
    l2=[]
    while True:
        if m in l[:len(l)//2]:
            ind=l.index(m)
            d=(len(l)//2)-(ind+1)
            for i in range(len(l)//2):
                d+=1
                l1.append(d)
            l[ind]=0
        else:
            break
    while True:
        if m in l[len(l)//2:]:
            ind=l[len(l)//2:].index(m)
            d=(len(l)//2)-(ind+1)
            for i in range(len(l)//2):
                d+=1
                l2.append(d)
            l[len(l)//2+ind]=0
        else:
            break
    c=0
    for i in set(l1):
        if i not in set(l2):
            c+=1
    print(c)
"""
t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    if l.count(m)==1:
        print(n//2)
    else:
        l1=[]
        for i in range(n):
            if m in l:
                ind=l.index(m)
                l1.append(ind+1)
                l[ind]=0
        l2=[]
        for i in range(len(l1)-1):
            l2.append(l1[i+1]-l1[i])
        l2.append(l1[0]-(n-l1[-1]))
        if max(l2)>n//2:
            print((n//2)-(sum(l2)-max(l2)))
        else:
            print(0)