"""
s=input()
s2=0
s1=''
k=1
for i in s:
    s1=''
    s1=i
    for j in s[k:]:
        s1+=j
        s2+=int(s1)
    k+=1
sm=0
x=int(s)
while x>0:
    a=x%10
    sm+=a
    x//=10
print(s2+sm)
"""
s=input()
m=10**9+7
sm=0
s1='1'*len(s)
for i in range(len(s)):
    sm+=(int(s[i])%m)*((i+1)%m)*(int(s1)%m)
    s1=s1[:-1]
print(sm%m)

