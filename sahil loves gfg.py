"""
t=int(input())
while t:
    t-=1
    c=0
    s=input()
    while True:
        if 'gfg' in s:
            c+=1
            s=s.replace('gfg','g',1)
        else:
            if c==0:
                print(-1)
                break
            else:
                print(c)
                break
"""
l=[1,2,2,3,4]
x=l.count(2)
l.remove(2,x)
print(l)

"""
t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    print(sum(s))
"""