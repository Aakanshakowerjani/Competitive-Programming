t=int(input())
while t:
    t-=1
    a,b,c,n=map(int,input().split())
    if n==0:
        if a==b==c:
            print('YES')
        else:
            print('NO')
    else:
        if a>b:
            if a>c:
                x=n-((a-c)+(a-b))
            else:
                x=n-((c-a)+(c-b))
        else:
            x=n-((b-a)+(b-c))
        if x%3==0:
            print('YES')
        else:
            print('NO')