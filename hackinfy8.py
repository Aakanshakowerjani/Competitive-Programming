"""
l=list(map(int,input().split()))
n=l[0]
k=l[-1]
l=l[1:-1]
l1=[]
s1='Sam wins the game of '+str(n)+' pile(s).'
s2='Alex wins the game of ' +str(n)+ ' pile(s).'
c=-1
while True:
    if l==[0]*len(l):
        if c%2==0:
            print(s1)
            break
        else:
            print(s2)
            break
    else:
        if max(l)>k:
            l[l.index(max(l))]=max(l)-k
            c+=1
        else:
            l[l.index(max(l))]=0
            c+=1

"""
l=list(map(int,input().split()))
n=l[0]
k=l[-1]
l=l[1:-1]
c=-1
s1='Sam wins the game of '+str(n)+' pile(s).'
s2='Alex wins the game of ' +str(n)+ ' pile(s).'
for i in range(n):
    c+=l[i]//k
    if l[i]%k!=0:
        c+=1
if c%2==0:
    print(s1)
else:
    print(s2)