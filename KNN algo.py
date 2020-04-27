import math
n=int(input('enter no of indegrents'))
l=[]
for i in range(n):
    indi=input('enter indegrent')
    s,c=map(int,input('enter its sweetness and chrunchiness').split())
    f_type=input('enter food type')
    l.append([indi,s,c,f_type])
ind=input('enter predicted ingridient')
sw,cr=map(int,input('enter its sweetness and crunchiness').split())
l2=[]
for i in l:
    l2.append([math.sqrt((sw-i[1])**2 + (cr-i[2])**2),i[3]])
min=l2[0][0]
for i in l2:
    if i[0]<min:
        min=i[0]
        predict=i[1]
print(predict)