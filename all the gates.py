
t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    l=list(map(str,input().split()))
    for i in range(k):
        if l[-1]=='T':
            l=l[:-1]
        elif l[-1]=='H':
            for j in range(len(l)):
                if l[j]=='T':
                    l[j]='H'
                else:
                    l[j]='T'
            l=l[:-1]
    print(l.count('H'))
"""
t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    s=input().split()
    s1=str(s)
    for i in range(k):
        if s1[-1] == 'T':
            s1 = s1[:-1]
        elif s1[-1] == 'H':
            s1.replace('H','T')
            s1.replace('T','H')
            s1=s1[:-1]
    print(s1.count('H'))
"""