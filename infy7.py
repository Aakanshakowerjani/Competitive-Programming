"""
s=input()
for i in range(1,len(s)):
    if s[i]==')' and s[i-1]=='(':
        s=s.replace(s[i],'')
        s=s.replace(s[i-1],'')
    elif s[i]=='}' and s[i-1]=='{':
        s.replace(s[i],'')
        s.replace(s[i-1],'')
    elif s[i] == ']' and s[i - 1] == '[':
        s=s.replace(s[i],'')
        s=s.replace(s[i - 1],'')
    elif s[i]=='}' or s[i]==']' or s[i]==')' or len(s)==1:
        print(i+1)
        break
if len(s)==0 :
    print(0)


    """
import copy
n=int(input('max no of swaps'))
l=list(map(int,input('list of nos').split()))
x=[]
x=copy.copy(l)
s=0
for i in range(len(l)):
    s+=len(l)-l.index(max(l))
    l.remove(max(l))
if n>s:
    x.sort()
    print(x)
else:
    print('Cnt be done')