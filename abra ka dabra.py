l=int(input())
s=input()
for i in range(len(s)):
    s=s.replace('ab','')
print(len(s))