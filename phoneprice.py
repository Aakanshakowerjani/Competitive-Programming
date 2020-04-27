"""
#l=[350,360,467,455,444,432,412,367]
l=[766,750,723,662,647,656,619]
if l[0]<l[1]:
    min=l[0]
    smin=l[1]
else:
    min=l[0]
    smin=l[1]

c=1
for i in range(2,len(l)):
    if i >= 5:
        if l[i-5] == min:
            min=smin
            smin=l[i]
            if l[i] <min:
                smin=min
                min=l[i]
                c+=1
        elif l[i-5] == smin:
            smin=0
        elif l[i] < min:
            smin = min
            min = l[i]
            c += 1
    elif l[i] <min:
        smin=min
        min=l[i]
        c+=1
    elif l[i]<smin:
        smin=l[i]
print(c)
"""
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    for i in range(1,n):
        if i<=4:
            if l[i]<min(l[:i]):
                c+=1
        else:
            if l[i]<min(l[i-5:i]):
                c+=1
    print(c)
