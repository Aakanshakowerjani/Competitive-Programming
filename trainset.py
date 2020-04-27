t=int(input())
while t:
    t-=1
    N=int(input())
    l=[]
    l1=[]
    for i in range(N):
        l.append(input().split())
    for j in l:
        l1.append(j[0])
    s=set(l1)
    sum1=0
    for i in s:
        c1 = 0
        c2 = 0
        for j in l:
            if j[0] == i:
                if j[1] == '0':
                    c1+=1
                else:
                    c2+=1
        if c1>c2:
            sum1+=c1
        else:
            sum1+=c2
    print(sum1)