s=input()
i=0
while True:
    if i+1<len(s):
        if s[i]==s[i+1] or s[i]==s[i-1]:
            s=s.replace(s[i],'',2)
        else:
            i+=1
    else:
        break
if len(s)==0:
    print('Empty String')
else:
    print(s)
