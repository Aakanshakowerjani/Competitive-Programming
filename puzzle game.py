# cook your dish here
t = int(input())
while t:
    t -= 1
    l = []
    c=0
    l.extend(map(int, input().split()))
    l.extend(map(int, input().split()))
    l.extend(map(int, input().split()))
    for i in range(1,10):
        if l[i-1]!=i:
            c+=1
    if c==9:
        print(-1)
    else:
        print(c)