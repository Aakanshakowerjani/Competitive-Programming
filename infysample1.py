from itertools import permutations
s=input().split(',')
comb=permutations(s,3)
s1=set()
for i in comb:
    s1.add(i)
l=len(s)
s.sort(reverse=True)
for i in s[:3]:
    print(i,end='')
print(',', end='')
print(l)
