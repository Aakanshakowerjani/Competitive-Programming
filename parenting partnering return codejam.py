"""
x=1
import copy
t=int(input())
while t:
    t-=1
    n=int(input())
    lst2=[]
    for i in range(n):
        l=list(map(int,input().split()))
        lst2.append(l)
    lst=lst2.copy()
    lst.sort()
    j1=lst[0][0]
    j2=lst[0][1]
    s='J'
    c1=0
    c2=0
    f=0
    res=''
    for i in range(1,n):
        if j2>lst[i][0] and c2>lst[i][0]:
            f=1
            break
        elif j2>lst[i][0]:
            c1=lst[i][0]
            c2=lst[i][1]
            s+='C'
        elif c2>lst[i][0]:
            j1=lst[i][0]
            j2=lst[i][1]
            s+='J'
        else:
            j1=lst[i][0]
            j2=lst[i][1]
            s+='J'
    if f==1:
        print('Case #', end='')
        print(x, end='')
        print(':', 'IMPOSSIBLE')
    else:
        for i in range(n):
            res+=s[lst.index(lst2[i])]
        print('Case #', end='')
        print(x, end='')
        print(':', res)
    x += 1

x = 1
t = int(input())
while t:
    t -= 1
    n = int(input())
    j=[]
    c=[]
    res=''
    for i in range(n):
        s,e=map(int,input().split())
        if len(j)==0 or (not any([(s>=S and s<E) for S,E in c])):
            c.append([s,e])
            res+='C'
        elif len(j)==0 or (not any([(s>=S and s<E) for S,E in j])):
            c.append([s,e])
            res+='J'
        else:
            res='IMPOSSIBLE'
            break
    print(res)
    """
import copy
x=1
t=int(input())
while t:
    t-=1
    n=int(input())
    lst2=[]
    for i in range(n):
        l=list(map(int,input().split()))
        lst2.append(l)
    lst=lst2.copy()
    lst.sort()
    j1=lst[0][0]
    j2=lst[0][1]
    s='J'
    c1=0
    c2=0
    f=0
    res=''
    for i in range(1,n):
        if lst[i][0]>=j1 and j2>lst[i][0] and lst[i][0]>=c1 and c2>lst[i][0]:
            f=1
            break
        elif lst[i][0]>=j1 and j2>lst[i][0]:
            c1=lst[i][0]
            c2=lst[i][1]
            s+='C'
        elif lst[i][0]>=c1 and c2>lst[i][0]:
            j1=lst[i][0]
            j2=lst[i][1]
            s+='J'
        else:
            j1=lst[i][0]
            j2=lst[i][1]
            s+='J'
    if f==1:
        print('Case #', end='')
        print(x, end='')
        print(':', 'IMPOSSIBLE')
    else:
        for i in range(n):
            res+=s[lst.index(lst2[i])]
            ind=lst.index(lst2[i])
            lst[ind]=0
        print('Case #', end='')
        print(x, end='')
        print(':', res)
    x += 1