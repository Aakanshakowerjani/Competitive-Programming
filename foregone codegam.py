"""
t = int(input())
while t:
    t -= 1
    n = int(input())
    for i in range(n - 1):
        if '4' not in str(i):
            if '4' not in str(n-i):
                print(i, n-i)
                break

n=int(input())
x=n
s=''
while n>0:
    if n%10==4:
        s+=str(1)
    else:
        s+=str(0)
    n//=10
print('Case #',end="")
print(x,end="")
print(':',end=" ")
print(int(s[::-1]),x-int(s[::-1]))

s=input()
s1=''
if s[0]=='#':
    s=s[1:]

for i in s:
    if i!='#':
        s1+=i
    else:
        s1=s1[:-1]
print(s1)
"""
l1=[1,2,23,4,5]
l2=[1,2,5,23,6]
k=1
for i in l2:
    if i not in l1:
        k=0
        break
print(str(bool(k)).lower())