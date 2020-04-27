t=int(input())
while t:
    t-=1
    l=['h','a','c','k','e','r','r','a','n','k']
    l=l[::-1]
    x=0
    s=input()
    for i in s:
        if len(l)==0:
            x=1
            break
        elif i==l[-1]:
            l.pop()
    if x==0:
        if len(l)==0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')