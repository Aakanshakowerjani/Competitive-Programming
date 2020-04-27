t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    if m<n:
        if len(l)==len(set(l)):
            print('YES')
        else:
            print('NO')
    else:
        c=0
        for i in l[::n]:

            if len(l[i:i+3])!=len(set(l[i:i+3])):
                print(l[i:i+3])
                print(len(l[i:i+3]),len(set(l[i:i+3])))
                print('hello')
                c=1
                break
        if c==0:
            print('YES')
        else:
            print('NO')