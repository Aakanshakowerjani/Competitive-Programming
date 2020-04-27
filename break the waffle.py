"""
n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
sm1=0
sm2=0
sm1+=sum(n1)
sm2+=sum(m1)
n1=n1*m
m1=m1*n
sm1+=sum(m1)
sm2+=sum(n1)
if sm1>sm2:
    print(sm2)
else:
    print(sm1)
"""
def Max_list(L1,L2):
    M1=max(L1)
    M2=max(L2)
    if M1>=M2:
        return  L1.index(M1),1
    else:
        return L2.index(M2),2
S=0
M,N=list(map(int,input().split()))
if M<=0 or N<=0:
    print(0)
L1=list(map(int,input().split()))
M1=1
L2=list(map(int,input().split()))
M2=1
while max(L1)!=-1 or max(L2)!=-1:
    Index,I=Max_list(L1,L2)
    if I==1:
        S=S+(L1[Index]*M1)
        M2=M2+1
        L1[Index]=-1
    else:
        S=S+(L2[Index]*M2)
        M1=M1+1
        L2[Index]=-1
print(S)