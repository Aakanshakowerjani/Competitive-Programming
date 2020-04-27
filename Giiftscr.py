t=int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    if s[0]=='L':
        x=-1
        y=0
    elif s[0]=='R':
        x=1
        y=0
    elif s[0]=='U':
        x=0
        y=1
    else:
        x=0
        y=-1
    for i in range(1,len(s)):
        if (s[i-1]=='L' or s[i-1]=='R') and s[i]=='U':
            y+=1
        elif (s[i-1]=='L' or s[i-1]=='R') and s[i]=='D':
            y-=1
        elif (s[i-1]=='U' or s[i-1]=='D') and s[i]=='L':
            x-=1
        elif (s[i-1]=='U' or s[i-1]=='D') and s[i]=='R':
            x+=1
    print(x,y)

