"""
n=int(input())
l=list(map(int,input().split()))
c=1
a=l[0]
for i in l:
    if i==a:
        a-=1
    else:
        c+=1
        a=i-1
print(c)
"""
n=int(input())
l=list(map(int,input().split()))
c=1
a=l[0]
l.remove(a)
while True:
    if len(l)==0:
        break
    else:
        if a-1 in l:
            l.remove(a-1)
            a-=1
        else:
            c+=1
            a=l[0]
            l.remove(a)
print(c)