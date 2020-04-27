l=list(map(int,input().split()))
if l[0]<1:
    st=abs(l[0])+1
else:
    st=1
i=st
ind=0
while True:
    i=l[ind]+i
    if i<1:
        ind=0
        st+=1
        i=st
    else:
        ind+=1
    if ind>=len(l):
        print(st)
        break