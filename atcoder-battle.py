"""
a, b, c, d = map(int, input().split())
i = 1
while True:
    if a <= 0:
        print('No')
        break
    elif c <= 0:
        print('Yes')
        break
    if i % 2 == 0:
        a -= d
    else:
        c -= b
    i+=1
"""
n=int(input())
st=set()
for i in range(n):
  s=input()
  st.add(s)
print(len(st))