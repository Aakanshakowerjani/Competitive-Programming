t=int(input())
while t:
    t-=1
    m,k=map(int,input().split())
    l=list(map(int,input().split()))
    l2=['YES']
    n=m-1
    l2.extend([0]*m)
    for i in range(m):
        if k%l[n-i]==0 and len(l)==1:
            print('NO')
            break
        elif l[n-i]>k:
            l2[n-i+1]=1
            print(*l2)
            break
        else:
            if k%l[n-i]==0:
                l2[n-i+1]=int(k/l[n-i])-1
                k=l[n-i]
                l.pop()
            else:
                l2[n-i+1]=int(k/l[n-i]+1)
                print(*l2)
                break
"""
t=int(input())
while t:t=int(input())
while t:
    t-=1
    m,k=map(int,input().split())
    l=list(map(int,input().split()))
    l2=['YES']
    n=m-1
    l2.extend([0]*m)
    for i in range(m):
        if k%l[n-i]==0 and len(l)==1:
            print('NO')
            break
        elif l[n-i]>k:
            l2[n-i+1]=1
            print(*l2)
            break
        else:
            if k%l[n-i]==0:
                l2[n-i+1]=int(k/l[n-i])-1
                k=l[n-i]
                l.pop()
            else:
                l2[n-i+1]=int(k/l[n-i]+1)
                print(*l2)
                break
    t-=1
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    ls=['YES']
    for i in range(n):
        ls.append(0)
    c=0
    for i in range(n):
        if k%l[i]!=0:
            ls[i+1]=int(k/l[i])+1
            break
        else:
            c+=1
    if c==n:
        print('NO')
    else:
        print(*ls)
"""
