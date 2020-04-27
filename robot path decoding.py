x=1
t=int(input())
while t:
    t-=1
    dig = []
    ind = []
    s = input()
    i = 0
    while True:
        if i >= len(s):
            break
        if s[i].isdigit():
            dig.append(int(s[i]))
            i += 1
        elif s[i] == '(':
            ind.append(i)
            i += 1
        elif s[i] == ')':
            s = s[:ind[-1] - 1] + s[ind[-1] + 1:i] * dig[-1] + s[i + 1:]
            dig.pop()
            ind.pop()
            i += 1
        else:
            i += 1
    w=1
    h=1
    for i in s:
        if i=='W':
            if w==1:
                w=1000000000
            else:
                w-=1
        elif i=='E':
            if w==1000000000:
                w=1
            else:
                w+=1
        elif i=='S':
            if h==1000000000:
                h=1
            else:
                h+=1
        elif i=='N':
            if h==1:
                h=1000000000
            else:
                h-=1
    print('Case #', end='')
    print(x, end='')
    print(':', w,h)
    x += 1
