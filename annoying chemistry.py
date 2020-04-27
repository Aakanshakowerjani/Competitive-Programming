x,y,p,q=map(int,input().split())
b1=1
b2=1
b3=1
while True:
    if (b1*x==b3*p) and (b2*y==b3*q):
        print(b1,b2,b3)
        break
    else:
        if (p*b3)%(x*b1)==0:
            b1*=int((p*b3)/(x*b1))
        else:
            m=p*b3
            b3*=(x*b1)
            b1*=m
        if (q*b3)%(y*b2)==0:
            b2*=int((q*b3)/(y*b2))
        else:
            n=q*b3
            b3*=(y*b2)
            b2*=n