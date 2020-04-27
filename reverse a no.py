"""
t=int(input())
while t:
    t-=1
    r=0
    n=int(input())
    while n>0:
        a=n%10
        r=r*10+a
        n=n//10
    print(r)

while True:
    a=int(input())
    if a==42:
        break
    else:
        print(a)


t=int(input())
while t:
    t-=1
    s=input()
    n=len(s)
    if n%2==0:
        l1=list(s[:n//2])
        l2=list(s[n//2:])
    else:
        l1=list(s[:n//2])
        l2=list(s[(n//2)+1:])
    l1.sort()
    l2.sort()
    x=0
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            x=1
            break
    if x==0:
        print('YES')
    else:
        print('NO')


l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
l1=[]
for i in range(n):
    l1.append(l[i]*(i+1))
print(max(l1))


t=int(input())
while t:
    t-=1
    k,a,b=map(int,input().split())
    x=(a+b)%10
    s=a+b
    if k==2:
        if x%3==0:
            print('YES')
        else:
            print('NO')
    else:
        s+=x
        s+=(((k-3)//4)*20)
        f=(k-3)%4
        while f:
            f-=1
            x=(2*x)%10
            s+=x
        if s%3==0:
            print('YES')
        else:
            print('NO')

"""

def mul(K, a,b):
    s = 0
    t = (a+b) % 10
    s = a+b
    if (K == 2):
        if (s% 3 == 0):
            return True
        else:
            return False

    s += t
    ng = (K - 3) // 4
    rd= (K - 3) % 4
    s += (ng * 20)
    for i in range(rd):
        t = (2 * t) % 10
        s += t
    if (s % 3 == 0):
        return True
    else:
        return False

t=int(input())
while t:
    t-=1
    k,a,b=map(int,input().split())
    if mul(k,a,b):
        print('YES')
    else:
        print('NO')