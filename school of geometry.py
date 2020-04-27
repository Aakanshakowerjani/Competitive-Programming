""""
t=int(input())
while t:
    t-=1
    n=int(input())
    A=sorted(map(int,input().split()))
    B=sorted(map(int,input().split()))
    s=0
    for i in range(n):
        if A[i]<B[i]:
            s+=A[i]
        else:
            s+=B[i]
    print(s)
"""
print(41%7)
print(4%7)
print(6%5)
print(9%5)

