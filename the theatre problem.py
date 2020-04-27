import copy
t=int(input())
final1=[]
while t:
    t-=1
    n=int(input())
    final=[]
    l=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(n):
        s=input()
        movie=s[0]
        time=int(s[2])
        l[ord(movie)-65][int(time/3)-1]+=1
    lis=[]
    for i in range(4):
        s=0
        lis.append(l[i][0])
        for j in range(4):
            if j!=i:
                lis.append(l[j][1])
                for k in range(4):
                    if k!=i and k!=j:
                        lis.append(l[k][2])
                        for m in range(4):
                            if m!=i and m!=j and m!=k:
                                lis.append(l[m][3])
                        s=0
                        s-=(lis.count(0))*100
                        lis1=copy.deepcopy(lis)
                        lis1.sort()
                        c=0
                        for p in lis1[::-1]:
                            s+=p*(100-25*c)
                            c+=1
                        final.append(s)
                        lis=lis[:2]
                lis=lis[:1]
        lis=[]
    print(max(final))
    final1.append(max(final))
print(sum(final1))
"""
import copy
from itertools import permutations
t=int(input())
final=[]
while t:
    t-=1
    n=int(input())
    l=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(n):
        s=input()
        movie=s[0]
        time=int(s[2])
        l[int(time/3)-1][ord(movie)-65]+=1
    comb=permutations([0,1,2,3],4)
    l2=[]
    l3=[]
    l3=copy.deepcopy(l)
    for i in comb:
        s=0
        for j in range(len(i)):
            if max(l3[i[j]])==0:
                s-=100
            else:
                s+=max(l3[i[j]])*(100-(25*j))
                ind=l3[i[j]].index(max(l3[i[j]]))
                for k in l3:
                    k[ind]=0
        l3=[]
        l3=copy.deepcopy(l)
        l2.append(s)
    final.append(max(l2))
    print(max(l2))
sm=0
for i in final:
    sm+=i
print(sm)

t=int(input())
while t:
    t-=1
    n=int(input())
    l=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(n):
        s=input()
        movie=s[0]
        time=int(s[2])
        l[ord(movie)-65][int(time/3)-1]+=1
    l2=[]
    for i in l:
        l2.extend(i)
    s=0
    for i in range(4):
        m=0
        for j in range(l2):
            if l2[j]>m:
                m=l2[j]
                ind=j
        s+=m*(100-(25*i))
        x=(ind+1)%4
"""