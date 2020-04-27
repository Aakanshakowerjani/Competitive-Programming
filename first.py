l=[375,750,723,662,647,656,619]
"""
m=[l[0]]
for i in range(0,len(l)-4):
    min=l[i]
    for j in range(0,5):
        if l[i+j] < min:
            m.append(l[i+j])
print(m)
s=set(m)
print(len(s))
"""
c=1
m=[l[0]]
for i in range(len(l)):
    print(min(l[0:i+1]))
    for j in range(0,5):
        if min(l[j:i+1]) not in m:
            m.append(l[i])
            c+=1
print(m)
print(c)