t=int(input())
while t:
    t-=1
    s=''
    plst=[]
    n=int(input())
    for i in range(n):
        plst.append(input())
    for p in plst:
        if len(s) == 0 or (len(s) == 1 and s[0] == '*'):
            s = ''
            s += p
        else:
            if p[0] == '*' and p[-1] == '*' and '*' in s:
                s = s[:s.index('*')] + p[1:-1] + s[s.index('*') + 1:]
            elif p[0] == '*':
                s += p[1:]
            elif p[-1] == '*' and s[0] == '*':
                s = p[:-1] + s[1:]
            elif '*' not in p:
                s = s.replace('*', '')
                if s == p:
                    s = p
                else:
                    s = '1'
                    break
    if len(s)==1 and s[0]=='1':
        print('*')
    else:
        s=s.replace('*','')
        print(s)
