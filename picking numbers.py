t=int(input())
l=list(map(int,input().split()))
m=0
s=set(l)
if len(set(l))==1:
    print(t)
else:
    l1=list(s)
    l1.sort()
    for i in l1:
        c=0
        if i+1 in l1:
           c+=l.count(i)
           c+=l.count(i+1)
        else:
            c+=l.count(i)
        if c>m:
            m=c
    print(m)
