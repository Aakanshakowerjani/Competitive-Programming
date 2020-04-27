t=int(input())
while t:
    t-=1
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1.sort()
    l2.sort()
    j=0
    c=0
    i=0
    while i<n :
        if l1[i]>l2[j]:
            c+=1
            i+=1
            j+=1
        else:
            i+=1
    print(c)
