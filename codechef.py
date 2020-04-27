
print(int('1010',2))
x=28
y=10
print(((x | y) &  (~x | ~y)))
print(x & y)
"""
# cook your dish here
t=int(input())
while(t):
    t-=1
    a=int(input(),2)
    b=int(input(),2)
    c=0
    if b=='0':
        c=0
    else:
        while(b!=0):
            c+=1
            u=a^b
            v=a & b
            a=u
            b=v*2
    print(c)
    """