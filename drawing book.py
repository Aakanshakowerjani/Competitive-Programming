n=int(input())
p=int(input())
if n%2==0:
    if p<=n/2:
        print(int(p/2))
    else:
        print(int((n-p)/2))
else:
    if int(n/2)+1<=p:
        print(int((n - p) / 2))
    else:
        print(int(p/2))