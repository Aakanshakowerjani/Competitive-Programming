t=int(input())
while t:
    t-=1
    l1=[0,0]
    l2=[0,0]
    a,b=map(int,input().split())
    l=[a+b,int(a//10)+((b%10)*10)+a%10+(int(b//10)*10),((a%10)*10)+int(b//10)+(b%10)+(int(a//10)*10)]
    print(max(l))