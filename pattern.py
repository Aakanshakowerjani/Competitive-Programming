n=9
for i in range(n-1,0,-1):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(0,(n-1)*2-(i*2)):
        print("#",end="")
    for m in range(0,i+1):
        print("*",end="")
    print()
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    for k in range(0,(n-1)*2-(i*2)):
        print("#",end="")
    for m in range(0,i+1):
        print("*",end="")
    print()



