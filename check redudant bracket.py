s=input()
c=0
x=0
c1=0
c3=0
c2=0
for i in range(len(s)):
    if s[i]=='(':
        c+=1
        c3+=1
        c1=0

    elif s[i]==')':
        c1+=1
        c2+=1
    elif c1==c3 and c!=1:
        x=1
        break
    elif c==c2 and i!=len(s)-1:
        c=0
        c2=0
        c3=0
        c1=0
    else:
        c1=0
        c3=0
if x==1:
    print('true')
else:
    print('false')