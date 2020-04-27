from itertools import combinations
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
comb=combinations(l,2)
c=0
l1=[]
for i in comb:
    if (i[0]+i[1])%k==0:
        c+=1
        l1.append([i[0],i[1]])
print(c)
print(l1)