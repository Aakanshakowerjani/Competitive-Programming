"""
n=int(input())
s=0
for i in range(n):
  if ((i+1) % 3 ==0) or ((i+1) % 5==0):
    pass
  else:
    s+=(i+1)
print(s)


def findMaxGCD(arr, n):
  high = 0
  for i in range(0, n):
    high = max(high, arr[i])
  count = [0] * (high + 1)
  for i in range(0, n):
    count[arr[i]] += 1
  counter = 0
  for i in range(high, 0, -1):
    j = i
    while (j <= high):
      if (count[j] > 0):
        counter += count[j]
      j += i
      if (counter == 2):
        return i
    counter = 0
arr = [2,3,4,4,4]
n = len(arr)
print(findMaxGCD(arr, n))

t=int(input())
while t:
  t-=1
  n=int(input())
  l=list(map(int,input().split()))
  m=max(l)
  c=[0]*(m+1)
  for i in range(n):
    c[l[i]]+=1
  cnt=0
  for i in range(m,0,-1):
    j=i
    while j<=m:
      if c[j]>0:
        cnt+=c[j]
      j+=i
      if cnt==2:
        print(i)
        break
    cnt=0

def dc(x,y):
  while y:
    x,y=y,x%y
  return x
t=int(input())
while t:
  t-=1
  n=int(input())
  m=0
  l=list(map(int,input().split()))
  for i in range(1,n):
    if dc(l[i],l[i-1])>m:
      m=dc(l[i],l[i-1])
  print(m)

t=int(input())
while t:
    t-=1
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        st=input()
        op=st[0]
        ch=st[2]
        k=int(st[4])
        c=0
        sm=0
        lg=0
        for j in range(n):
            if s[j]==ch:
                c+=1
                if c==k:
                    sm=j+1

                elif c==k+1 or j==n-1:
                  lg=j
                  break
        if op=='S':
            print(sm)
        else:
            print(lg)
       """
t=int(input())
while t:
    t-=1
    n,q=map(int,input().split())
    s=input()
    for i in range(q):
        st=input()
        op=st[0]
        ch=st[2]
        k=int(st[4])
        c=0
        sm=0
        lg=0
        if op=='S':
          for j in range(n):
            if s[j]==ch:
                c+=1
                if c==k:
                    sm=j+1
          print(sm)
        elif op=='L':
          for j in range(n):
            if s[j]==ch:
                c+=1
                if c==k:
                    if ch in s[j+1:]:
                      ind=s[j+1:].index(ch)
                      print(j+1+ind)
                    else:
                      print(n)
