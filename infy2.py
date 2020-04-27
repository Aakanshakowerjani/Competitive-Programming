"""
l=[2,6,3,5,8,9]
for i in range(len(l)):
    if i+1<=len(l) and l[i]+l[i+1] in l:
"""
l=['a','A','b','B']
for i in range(len(l)):
    l[i]=l[i].lower()

s=set(l)
print(s)