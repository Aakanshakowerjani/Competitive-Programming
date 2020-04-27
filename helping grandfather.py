r,c,xr,xc=map(int,input().split())
s1=''
l=[]
for i in range(r):
    s=input()
    s1=''
    for i in s:
        s1+=i*xc
    for i in range(xr):
        l.append(s1)
for i in l:
    print(i)