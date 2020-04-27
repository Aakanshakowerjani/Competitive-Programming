t=int(input())
n,q=map(int,input().split())
n1=list(map(int,input().split()))
q1=list(map(int,input().split()))
l=[]
m=n1[0]
for i in n1:
    if m<i:
        l.append(i)
        m=i
    else:
        l.append(m)
print(l)
for i in q1:
    print(l[i-1])