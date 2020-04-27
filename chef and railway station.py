from itertools import combinations
t=int(input())
while t:
    t-=1
    cnt=0
    n,m=map(int,input().split())
    n1=list(map(int,input().split()))
    m1=list(map(int,input().split()))
    comb1=combinations(n1,2)
    comb2=combinations(m1,2)
    f=0
    for i in n1:
        for j in comb2:
            f+=1
            print(n1)
            print(i)
            print(j)
            a=(j[0]-j[1])**2
            b=(i**2)+(j[0]**2)
            c=(i**2)+(j[1]**2)
            if a>b:
                if a>c:
                    if a==b+c:
                        cnt+=1
                        print(a,b,c,1)
                else:
                    if c==a+b:
                        cnt+=1
                        print(a,b,c,1)
            else:
                if b>c:
                    if b==a+c:
                        cnt+=1
                        print(a,b,c,1)
                else:
                    if c==a+b:
                        cnt+=1
                        print(a,b,c,1)
    print(m1)
    print(comb1)
    for i in m1:
        for j in comb1:
            f+=1
            print(i)
            print(j)
            a=abs(j[0]-j[1])**2
            b=(i**2)+(j[0]**2)
            c=(i**2)+(j[1]**2)
            if a>b:
                if a>c:
                    if a==b+c:
                        cnt+=1
                        print(a,b,c,2)
                else:
                    if c==a+b:
                        cnt+=1
                        print(a,b,c,2)
            else:
                if b>c:
                    if b==a+c:
                        cnt+=1
                        print(a,b,c,2)
                else:
                    if c==a+b:
                        cnt+=1
                        print(a,b,c,2)
    print(cnt)
    print(f)