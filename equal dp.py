t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    m=min(l)
    cnt=[]
    while m>=0:
        l1=[m]*n
        c=0
        for i in range(n):
            a=l[i]-l1[i]
            c+=a//5
            c+=(a%5)//2
            c+=((a%5)%2)//1
        cnt.append(c)
        m-=1
    print(min(cnt))