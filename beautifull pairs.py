"""
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
q=int(input())
for i in range(q):
    c=0
    x1,x2,y1,y2=map(int,input().split())
    for i in l:
        if i[0]>=x1 and i[0]<=x2 and i[1]>=y1 and i[1]<=y2:
            c+=1
    print(c)
"""
def check(a,n):
    if n==1:
        return True
    a.sort()
    d=a[1]-a[0]
    for i in range(2,n):
        if a[i]-a[i-1]!=d:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
if check(a,n):
    print('Yes')
else:
    print('No')