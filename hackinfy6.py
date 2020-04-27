"""
from itertools import permutations
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    l1.append(i)
comb=permutations(l1,n)
l2=[]
m=max(l)
for i in comb:
    for j in i[::2]:
        if j+1<len(i):
            if abs(l[j]-l[j+1])==0:
                m=0
                break
            elif m>abs(l[j]-l[j+1]):
                m=abs(l[j]-l[j+1])
print(m)
"""
import itertools as iter
def particles(li):
    global m
    if len(li) > 1:
        for i in iter.combinations(li, 2):
            temp = abs(i[0] - i[1])
            if m > temp:
                m = temp
            k = li.copy()
            k.remove(i[0])
            k.remove(i[1])
            k.append(temp)
            particles(k)
    else:
        return m
n = int(input())
lst = list(map(int,input().split()))
m = min(lst)
particles(lst,m)
print(m)