t=int(input())
while t:
    t-=1
    s=input()
    c=1
    s1=""
    for i in range(len(s)):
        if i+1 < len(s):
            if s[i] == s[i+1]:
                c+=1
            else:
                s1=s1+s[i]+str(c)
                c=1
        elif i+1 == len(s):
            if s[i]==s[i-1]:
                s1=s1+s[i]+str(c)
            else:
                s1=s1+s[i]+str(1)
    if len(s)<=len(s1):
        print("NO")
    else:
        print("YES")
