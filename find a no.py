import math
def pfctsq(x):
    sr=math.sqrt(x)
    return ((sr-math.floor(sr))==0)
def pro(x):
    p=1
    while x>0:
        a=x%10
        p*=a
        x//=10
    return p
t=int(input())
while t:
    t-=1
    j=0
    m=0
    a,b,k=map(int,input().split())
    for i in range(a,b+1):
        if pro(i)!=0 and pfctsq(pro(i)):
            j+=1
        if j==k:
            j=i
            m=1
            break
    if m==1:
        print(j)
    else:
        print(-1)