x=[1,2,3,4,5]
y=[3,4,2,4,5]
print('X', 'Y')
for i in range(5):
    print(x[i], y[i])
xm=sum(x)/5
ym=sum(y)/5
x1=[]
y1=[]
xy=[]
for i in range(5):
    xy.append(round((x[i]-xm)*(y[i]-ym),2))
    x1.append((x[i]-xm)**2)
    y1.append(round(y[i]-ym,2))
xy1=sum(xy)/5
x12=sum(x1)/5
m=xy1/x12
c=ym-(m*xm)
xx=input('enter value of x')
yy=m*int(xx)+c
print('predicted value of y is')
print(yy)