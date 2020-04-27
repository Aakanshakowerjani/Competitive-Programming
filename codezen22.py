l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=l1[:-1]
l2=l2[:-1]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
for i in l3:
    if i%2!=0:
        print(i,end=" ")
for i in l3:
    if i%2==0:
        print(i,end=" ")