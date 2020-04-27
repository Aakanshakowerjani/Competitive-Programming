"""
s=input()
s1=[]
s2=''
for i in range(len(s)):
    s2=''
    s2+=s[i]
    s1.append(s2)
    for j in range(i+1,len(s)):
        s2+=s[j]
        s1.append(s2)
print(s1)


s=input()
s1=[]
s2=0
for i in range(len(s)):
    s2=0
    s2+=ord(s[i])-96
    s1.append(s2)
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            s2+=ord(s[j])-96
            s1.append(s2)
print(set(s1))

"""

s=input()
s2=0
l=[]
i=0
while i<len(s):
    x=s[i]
    s2=0
    s2+=ord(s[i])-96
    l.append(s2)
    f=0
    for j in range(i+1,len(s)):
        if s[j]==s[i]:
            f+=1
            s2+=ord(s[i])-96
            l.append(s2)
        else:
            i+=f
            s2=0
            break
    i+=1
print(l)