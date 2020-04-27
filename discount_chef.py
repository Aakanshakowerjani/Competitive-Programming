t = int(input())
while (t):
    t -= 1
    s=input()
    if len(s) == 1:
        print(int(s))
    else:
        for i in range(len(s)):
            if int(s[i]) > int(s[i+1]) and i<len(s):
                s=int(s.replace(s[i],''))
                print(s)
                break




"""    
    n = list(map(int, input().split()))
    print(n)
    for i in range(len(n)):
        print(n,i)

    for i in range(len(n)):
        if n[i] > n[i + 1] and i < len(n):
            n.remove(n[i])
            print(n, endm="")
            break
"""
