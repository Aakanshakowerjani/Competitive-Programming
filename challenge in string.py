t=int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    a=s.count('A')
    b=s.count('B')
    c=0
    for i in range(len(s)):
        if i<a:
            if s[i]=='B':
                c+=1
        else:
            if s[i]=='A':
                c+=1
    print(min(a,b,c))