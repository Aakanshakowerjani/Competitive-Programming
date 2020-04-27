"""
i=0
t=int(input())
while t:
    i+=1
    t-=1
    a,b,c=map(int,input().split())
    while c>0:
        if c%a==b:
            print(i,c)
            break
        c-=1
"""
t=int(input())
while t:
    t-=1
    a,b,c=map(int,input().split())
    if (c%a)>=b:
        print(c-((c%a)-b))
    else:
        print((c-(c%a))-(a-b))

"""
print(322-54)
print(408-86)
print((322-54)%161)
print(407%161)
print(268%161)
print(161-107)
"""