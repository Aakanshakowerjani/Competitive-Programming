n,k=map(int,inpu().split())
x=n//k
if k==1:
    print('NO')
else:
    if x<k or x%k!=0:
        print('YES')
    else:
        print('NO')