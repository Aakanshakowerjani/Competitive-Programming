l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l3=['0','1','2','3','4','5','6','7','8','9']
s='abAG25$#hdk58(^^J'
s1=[]
s2=[]
c=0
for i in s:
    if (i in l) or (i in l1) or (i in l3):
        s1.append(i)
    else:
        s2.append(c)
    c+=1
for i in range(len(s)):
    if i in s2:
        print(s[i],end="")
    else:
        print(s1[-1],end="")
        s1.pop()