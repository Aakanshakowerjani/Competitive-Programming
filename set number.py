"""
print(bin(1000000000).replace('0b',''))
print(2**27)
l=[]
x=345
c=0
ele=x
for i in range(1,28):
    if (2**(i-1)) <=x and x<=(2**i):
        ind=i
print(2**(ind-1)-1)
for i in range(2**(ind-1)-1,x+1):
    if bin(i).count('1')>=c:
        c=bin(i).count('1')
        ele=i
print(ele)
print(bin(345))
print(bin(319))
print(bin(255))
"""
t=int(input())
while t:
    t-=1
    x=int(input())
    c = 0
    ele = x
    for i in range(1, 28):
        if (2 ** (i - 1)) <= x and x <= (2 ** i):
            ind = i
    for i in range(2 ** (ind - 1) - 1, x+1):
        if bin(i).count('1') >= c:
            c = bin(i).count('1')
            ele = i
    print(ele)

