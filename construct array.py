t=int(input())
while t:
    t-=1
    n,m=map(int,input().split())
    print(((m**n)-(m*(n-2)))%((10**9)+7))