t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    a=1
    tmp=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            tmp+=1
        else:
            a=max(a,tmp)
            tmp=1
    print(max(a,tmp))