t=int(input())
while t:
    t-=1
    a,b,c,n=map(int,input().split())
    if a>b:
        if a>c:
            x=(a-c)+(a-b)
        else:
            x=(c-a)+(c-b)
    else:
        x=(b-a)+(b-c)
    if n>0:
        if (n-x) % 3 == 0:
            print('YES')
        else:
            print('NO')
    else:
        if x==0:
            print('YES')
        else:
            print('NO')