"""
t=int(input())
while t:
    t-=1
    l=list(map(int,input().split()))
    n=l[0]
    m=l[1]
    l1=[]
    l2=[]
    l3=[]
    for i in range(n):
        l1.append(input().split())
    if n==m:
        if n%2!=0 and m%2!=0:
            ind=int(n/2)
            l2=l1[ind]
            for i in l1:
                l3.append(i[ind])
            if l2[::-1]==l2[::] and l3[::-1]==l3[::]:
                ans=(m*n)+1
            else:
                ans=(m*n)
        else:
            ans=m*n
    else:
        ans=m*n
    print(ans)

t = int(input())
while t:
    t -= 1
    l = list(map(int, input().split()))
    n = l[0]
    m = l[1]
    l1 = []
    s=0
    for i in range(n):
        l1.append(list(map(int , input().split())))
    for i in range(3,min(n+1,m+1),2):
        s+=(m-(i-1))*(n-(i-1))

"""
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(1,m-x-1):
    for j in range(1,n-x-1):
