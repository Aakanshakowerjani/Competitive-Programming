l=list(map(int,input().split()))
m=max(l)
l.remove(m)
x=m-l[0]
print(x,end=" ")
print(abs(l[1]-x),end=" ")
print(abs(l[2]-x),end=" ")