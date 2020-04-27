"""
t = int(input())
while t:
    t -= 1
    n = int(input())
    l = []
    for i in range(n):
        a = list(map(str, input().split()))
        a.sort()
        l.append(a)
    print(l)
"""
