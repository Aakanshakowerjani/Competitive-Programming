"""
t=int(input())
while t:
    t-=1
    s=input()
    l=list(s)
    c=0
    sa,sb=map(int,input().split())
    while l.index('A')<len(l) and l.index('B')>=0:
        ind1 = l.index('A')
        ind2 = l.index('B')
        if (ind1+sa)==(ind2-sb):
            c=1
            break
        else:
            l[ind1]='.'
            l[ind2]='.'
            if ind1+sa<len(l) and ind2-sb>=0:
                l[ind1+sa]='A'
                l[ind2-sb]='B'
            else:
                break
    if c==0:
        print('safe')
    else:
        print('unsafe')
    """
t=int(input())
while t:
    t=-1
    s=input()
    l=[]
    for i in s:
        l.append(i)
    print(l)
    sa,sb=map(int,input().split())
    x=l.index('A')
    y=l.index('B')
    for i in range(len(l)):
        if x<y:
            x+=sa
            y-=sb
        elif x==y:
            print('unsafe')
            break
        else:
            print('safe')
            break
