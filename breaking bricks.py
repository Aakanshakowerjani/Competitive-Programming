t=int(input())
while t:
    t-=1
    l=list(map(int,input().split()))
    s=l[0]
    w1=l[1]
    w2=l[2]
    w3=l[3]
    hit=1
    if w1+w2+w3<=s:
        hit=1
    elif w1+w2<=s or w2+w3<=s:
        hit+=1
    else:
        hit+=2
    print(hit)