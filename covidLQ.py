t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    l1=[]
    x=0
    for i in range(len(l)):
        if l[i]==1:
            l1.append(i)
    if len(l1)==1:
        print('YES')
    elif len(l1)==2:
        if l1[1]-l1[0]<6:
            print('NO')
        else:
            print('YES')
    else:
        for i in range(1,len(l1)):
            if l1[i]-l1[i-1]<6:
                x=1
                break
        if x==1:
            print('NO')
        else:
            print('YES')