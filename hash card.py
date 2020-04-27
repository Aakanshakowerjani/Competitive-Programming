t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for i in l:
        s+=i%k
    print(s%k)