def func(n):
    s=str(n)
    c=1
    s1=''
    if len(s)==1:
        s1=s1+str(c)+s
        return int(s1)
    else:
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                s1=s1+str(c)+s[i-1]
                c=1
            if i==len(s)-1:
                s1=s1+str(c)+s[-1]
        return int(s1)
n=int(input())
x=1
for i in range(1,n):
    x=func(x)
print(x)