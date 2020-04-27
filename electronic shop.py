b,n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
n2=list(filter(lambda x:x<b,n1))
n2.sort(reverse=True)
m2=list(filter(lambda x:x<b,m1))
m2.sort(reverse=True)
lst=[]
for i in n2:
    for j in m2:
        if i+j<=b:
            lst.append(i+j)
print(max(lst))