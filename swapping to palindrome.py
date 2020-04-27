t=int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    c=0
    for i in range(len(s)):
        if s==s[::-1]:
            print('YES')
            print(c)
            break
        elif len(s)==0 or len(s)==1:
            print('YES')
            print(c)
            break
        elif len(s)==2:
            if s[0]==s[1]:
                print('YES')
                print(c)
                break
            else:
                print('NO')
                break
        elif len(s)==3:
            if s[0]==s[-1]:
                print('YES')
                print(c)
                break
            else:
                if s[1]==s[0] or s[1]==s[-1]:
                    print('YES')
                    print(c+1)
                    break
                else:
                    print('NO')
                    break
        elif s[0]==s[-1]:
            if s[1]==s[-2]:
                s=s[2:-2]
            else:
                if len(s)-2<4:
                    if s[1]==s[2]:
                        print('YES')
                        print(c+1)
                        break
                    else:
                        print('NO')
                        break
                if s[1]==s[-3] and s[2]==s[-2]:
                    s=s[3:-3]
                    c+=1
                else:
                    print('NO')
                    break
        else:
            if s[0]==s[-2] and s[1]==s[-1]:
                s=s[2:-2]
                c+=1
            else:
                print('NO')
                break
