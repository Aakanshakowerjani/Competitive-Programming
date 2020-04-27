import random
t=100
print(t)
while t:
    t-=1
    n=random.randint(0,500)
    s=random.random('A','B')
    print(n)
    print(s)
    """
    a,b,c=random.randint(0,500),random.randint(0,500),random.randint(0,500)
    if b<a<c:
        print(a,b,c)
    for i in range(n):
        s,e=random.randint(0, 24 * 60),random.randint(0, 24 * 60)
        print(s,e)
    """