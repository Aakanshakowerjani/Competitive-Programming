t=int(input())
while t:
    t-=1
    n=int(input())
    l=[]
    for i in range(2,n):
        if n%i==0:
            if len(l)<2:
                l.append(i)
            else:
                break
    if len(l)!=2:
        print('NO')
    else:
        x=l[0]*l[1]
        if n%x==0:
            if int(n/x) in l:
                print('NO')
            else:
                print('YES')
                print(l[0],l[1],int(n/x))