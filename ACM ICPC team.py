from itertools import combinations

n,m=map(int,input().split())
l=[]
l2=[]
for i in range(n):
    l.append(input())
    l2.append(i)
per=combinations(l2,2)
m=0
lst=[]
for i in per:
    lst.append(list(bin((int(l[i[0]],2))|(int(l[i[1]],2)))).count('1'))
print(max(lst))
print(lst.count(max(lst)))
"""    
s1='100'
print(int(s1,2))






per=combinations([0,1,2,3],2)
for i in per:
    print(i)
    """