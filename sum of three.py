x=int(input())
l=list(map(int,input().split()))
l1=[]
s=0
for i in l:
    l1.append(abs(i-x))
for i in range(3):
    ind=l1.index(min(l1))
    s+=l[ind]
    l1.remove(min(l1))
    l.remove(l[ind])
print(s)
