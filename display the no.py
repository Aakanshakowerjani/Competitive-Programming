t=int(input())
l=[6,7,3,6,5,4,5,5,2,6]
while t:
    t-=1
    l1=[]
    n=int(input())
    for i in range(len(l)):
        if n==0:
            break
        elif l[i]<=n:
            x=n//l[i]
            if n%l[i]>=2:
                l1.extend([(9-i)]*x)
                n%=l[i]
            else:
                l1.extend([9-i]*(x-1))
                n=l[i]+(n%l[i])
    for i in l1:
        print(i,end='')