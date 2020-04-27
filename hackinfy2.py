l=list(map(float,input().split()))
l.sort()
l1=[]
c=0
while True:
    if len(l)==0:
        print(c)
        break
    elif l[-1]>1.99:
        c+=1
        l1.append([l[-1]])
        l.remove(l[-1])
    elif l[0]+l[-1]<=3:
            c+=1
            l1.append([l[0],l[-1]])
            l.remove(l[0])
            l.remove(l[-1])
print(l1)
