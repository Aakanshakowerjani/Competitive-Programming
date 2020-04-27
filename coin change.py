from itertools import permutations
n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
p=[]
s=set()
for i in l:
    print('hi')
    l1.extend([i]*n)
print(l1)
for i in range(1,n+1):
    p.append(permutations(l1,i))
for i in p:
    for j in i:
        x=list(j)
        x.sort()
        print(x)
        s.add(tuple(x))
c=0
for i in s:
    print(i)
    if sum(i)==n:
        c+=1
print(c)