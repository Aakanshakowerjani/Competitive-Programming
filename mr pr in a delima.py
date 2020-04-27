t=int(input())
while t:
    t-=1
    a,b,c,d=map(int,input().split())
    if a>b:
        if c>d:
            m1=b+c
            m2=a+d
        else:
            m1=b+d
            m2=a+c
    else:
        if c>d:
            m1=a+c
            m2=b+d
        else:
            m1=a+d
            m2=b+c
    while True:
        if m1==m2:
            print('YES')
            break
        elif m1>m2:
            print('NO')
            break
        else:
            m1+=max(c,d)
            m2+=min(c,d)