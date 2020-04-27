t=int(input())
while t:
    t-=1
    s1=[]
    s2=[]
    n,s=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    for i in range(n):
        if l2[i]==0:
            s1.append(l1[i])
        else:
            s2.append(l1[i])
    if len(s1)==0 or len(s2)==0:
        print('no')
    elif (100-s)>=(min(s1)+min(s2)):
        print('yes')
    else:
        print('no')