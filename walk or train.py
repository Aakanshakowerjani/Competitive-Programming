"""
# cook your dish here
t = int(input())
while t:
    t -= 1
    l = list(map(int, input().split()))
    n = l[0]
    a = l[1]
    b = l[2]
    c = l[3]
    d = l[4]
    p = l[5]
    q = l[6]
    y = l[7]
    t1 = 0
    l1 = list(map(int, input().split()))
    if c >= a and d <= b:
        if t1 == y:
            t1 += (d - c) * q
        else:
            t1 += (b - a) * p
    else:
        t1 += (b - a) * p
print(t1)

l=[0,0]
for j in range(128):
    if l[-1] in l[:-1]:
        x=[]
        for i in range(len(l)-1):
            if l[i]==l[-1]:
                x.append(i)
        l.append((len(l)-1)-x[-1])
    else:
        l.append(0)
print(l)

li=[8,7,9,5,7,8,8,8,5,7]
print(li[:-1])
li.pop()
lst=li[::-1]
ind=lst.index(7)+1
print(ind)
"""

# cook your dish here
t=int(input())
while t:
    t-=1
    N,a,b,c,d,P,Q,Y=map(int,input().split())
    path=list(map(int,input().split()))
    walk=abs(path.index(a)-path.index(b))*P
    if abs(path.index(a)-path.index(c)) <= Y:
        train=Y+abs(path.index(c)-path.index(d))*Q+abs(path.index(d)-path.index(b))*P
    else:
        train=walk+1
    if walk<train:
        print(walk)
    else:
        print(train)