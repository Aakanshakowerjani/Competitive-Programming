t = int(input())
x=1
while t:
    t -= 1
    s = 0
    r = 0
    c = 0
    l1 = []
    n = int(input())
    for i in range(n):
        l = list(map(int, input().split()))
        s += l[i]
        if len(set(l))!=n:
            r+=1
        l1.append(l)
    l3=[]
    for i in range(n):
        l3=[]
        for j in range(n):
            l3.append(l1[j][i])
        if len(set(l3))!=n:
            c+=1
    print('Case #',end='')
    print(x,end='')
    print(':',s,r,c)
    x+=1