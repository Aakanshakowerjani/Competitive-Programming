s=input()
c=0
s1=''
for i in s:
    if i=='z' or i=='a' or i=='p':
        l=len(s1)
        if l!=0:
            c+=int(l*(l+1)/2)
            s1=''
        else:
            c+=0
    else:
        s1+=i
l=len(s1)
if l!=0:
    c+=int(l*(l+1)/2)
r=int(len(s)*(len(s)+1)/2)
print(r-c)