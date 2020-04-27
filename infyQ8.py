d=['0','1','2','3','4','5','6','7','8','9']
s=input()
l=[]
for i in s:
    if i in d:
        l.append(i)
m=8
for i in l:
    if int(i)%2==0 and int(i)<m:
        m=int(i)
s=set(l)
s.remove(str(m))
s=list(s)
s.sort(reverse=True)
s.append(str(m))
for i in s:
    print(i,end='')