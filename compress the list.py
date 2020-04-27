"""
t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    final=[]
    l1=[]
    for i in range(len(l)):
        if i+1<len(l):
            if l[i]+1==l[i+1]:
                c+=1
                l1.append(l[i])
                l1.append(l[i+1])
            else:
                if c>=3:
                    final.append(l1[0])
                    final.append('...')
                    final.append(l1[-1])
                    final.append(',')
                    final.append(l[i+1])
                else:
                    final.append(l[i])
                    final.append(',')
                    #final.append(l[i+1])
            l1 = []
            c = 1
        else:
            final.append(l[-1])
    for i in final:
        print(i,end='')



t = int(input())
while t:
    t -= 1
    n = int(input())
    l =list(map(int,input().split()))
    x=""
    for i in range(len(l)):
        if i+1<len(l):
            if l[i]+1==l[i+1]:
                x+=str(l[i+1])
            else:
                if str(l[i]) in x:
                    x=x[:-1]
    print(x)

    s=''
    s+=str(l)
    s.replace(' ', '')
    for i in x:
        print(i)
        s.replace(i,'...')
        print(s)
    print(s)
    """
t=int(input())
while t:
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    l1=[]
    if len(l)==1:
        print(l[0])
        break
    for i in range(1,len(l)):
        if l[i-1]+1==l[i]:
            c+=1
        else:
            if c==0:
                l1.append(l[i-1])
                l1.append(',')
            elif c==1:
                l1.append(l[i-2])
                l1.append(',')
                l1.append(l[i-1])
                l1.append(',')
            else:
                l1.append(l[i-c-1])
                l1.append('...')
                l1.append(l[i-1])
                l1.append(',')
            c=0
    if c==0:
        l1.append(l[n-1])
    elif c ==1:
        l1.append(l[n-c-1])
        l1.append(',')
        l1.append(l[n-1])
    else:
        l1.append(l[n - c - 1])
        l1.append('...')
        l1.append(l[n - 1])
    for i in l1:
        print(i,end="")
    print()