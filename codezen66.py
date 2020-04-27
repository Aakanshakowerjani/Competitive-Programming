"""
n=int(input())
s=list(input())
s.insert(0,'0')
s.append('0')
for i in range(1,len(s)-1):
    if s[i]=='1':
        if s[i+1]=='0':
            s[i+1]='X'
            s[i] = 'X'
            s[i - 1] = 'X'
        else:
            s[i] = 'X'
            s[i - 1] = 'X'
print(s[1:-1].count('0'))
"""
num_ele = int(input())
elements = []
for ele in range(num_ele):
    elements.append(sorted(int(v) for v in input().split()))
