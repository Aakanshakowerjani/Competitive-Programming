"""
n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range(q):
    i=0
    sm=0
    l,r,d=map(int,input().split())
    while (r-(i*d))>=l:
        sm+=arr[r-(i*d)-1]
        i+=1
    print(sm)

n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range(q):
    sm=0
    l,r,d=map(int,input().split())
    if l<r:
        arr=arr[::-1]
        print(sum(arr[n-r:n-l+1:d]))
    else:
        print(sum(arr[n-l:n-r+1:d]))
"""
n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
q=int(input())
for i in range(q):
    l,r,d=map(int,input().split())
    print(sum(arr[r:l-1:-d]))

