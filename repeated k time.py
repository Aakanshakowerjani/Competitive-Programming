n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[0]*100001
for i in l:
    l1[i]+=1
for i in range(len(l1)):
    if l1[i]==k:
        print(i)
        break

n = int(input())
l = list(map(int, input().split()))
k = int(input())
s = set(l)
m = min(s)
while len(s) > 0:
    if l.count(m) == k:
        print(m)
        break
    else:
        s.remove(m)
        m = min(s)
