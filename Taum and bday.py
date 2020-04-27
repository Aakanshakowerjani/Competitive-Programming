t=int(input())
while t:
    t-=1
    b,w=map(int,input().split())
    bc,wc,z=map(int,input().split())
    if bc<wc:
        if bc+z<wc:
            print((w*(bc+z))+(b*bc))
        else:
            print((w*wc)+(b*bc))
    else:
        if wc+z<bc:
            print((b*(wc+z))+(w*wc))
        else:
            print((w*wc)+(b*bc))