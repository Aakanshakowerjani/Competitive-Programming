# cook your dish here
n=int(input())
l=list(map(int,input().split()))
m=l[0]
c=l[1]
x1=[]
x2=[]
for i in range(n):
    l1=list(map(int,input().split()))
    x=l1[0]
    y=l1[1]
    p=l1[2]
    y1=m*x+c
    if y>y1:
        x1.append(p)
    else:
        x2.append(p)
if sum(x1)>sum(x2):
    print(sum(x1))
else:
    print(sum(x2))