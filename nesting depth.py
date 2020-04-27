"""
t=int(input())
while t:
    t-=1
    s=input()
    if s[0]=='0':
        l=[0]
    else:
        l=['(']*int(s[0])
        l.append(int(s[0]))
        for i in range(int(s[0])):
            l.append(')')
    print(l)
    for i in range(1,len(s)):
        if s[i]>s[i-1]:
            len(l)

    """
t=int(input())
x=1
while t:
    t-=1
    s1=''
    s=input()
    if s[0]=='0':
        s1+='0'
    else:
        s1+=('('*int(s[0])+s[0]+')'*int(s[0]))
    for i in range(1,len(s)):
        if s[i]=='0':
            s1+='0'
        elif int(s[i])==int(s[i-1]):
            s1=s1[:(len(s1)-int(s[i-1]))]+s[i]+s1[(len(s1)-int(s[i-1])):]
        elif int(s[i])>int(s[i-1]):
            s1=s1[:(len(s1)-int(s[i-1]))]+'('*(int(s[i])-int(s[i-1]))+s[i]+')'*(int(s[i])-int(s[i-1]))+s1[(len(s1)-int(s[i-1])):]
        elif int(s[i])<int(s[i-1]):
            s1=s1[:(len(s1)-int(s[i]))]+s[i]+s1[(len(s1)-int(s[i])):]
    print('Case #', end='')
    print(x, end='')
    print(':',s1)
    x+=1