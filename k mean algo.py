l=list(map(int,input('enter dataset').split()))
n=int(input('emter value of k'))
m1,m2=map(int,input('enter m1 and m2').split())
div1=[]
div2=[]
while True:
    for i in l:
        a=abs(m1-i)
        b=abs(m2-i)
        if a>b:
            div2.append(i)
        else:
            div1.append(i)
    mean1=round(sum(div1)/len(div1))
    mean2=round(sum(div2)/len(div2))
    if m1==mean1 and m2==mean2:
        print(m1,m2)
        break
    else:
        m1=mean1
        m2=mean2
