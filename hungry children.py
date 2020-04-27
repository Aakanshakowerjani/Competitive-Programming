"""
n=int(input())
l=[]
c=0
for i in range(n):
    s=input()
    if s in l:
        if l.count(s)>len(l)-l.count(s):
            c+=1
            print(l)
    l.append(s)
print(c)

"""
mat=[]
row = int(input())
col=row
for i in range(row):
    mat.append(list(input()))
out=[]
for r in range(row):
    for c in range(col-2):
        if mat[r][c]==mat[r][c+1]==mat[r][c+2]:
            out.append(mat[r][c])
for r in range(row-2):
    for c in range(col):
        if mat[r][c]==mat[r+1][c]==mat[r+2][c]:
            out.append(mat[r][c])
for r in range(row-2):
    for c in range(col-2):
        if mat[r][c]==mat[r+1][c+1]==mat[r+2][c+2]:
            out.append(mat[r][c])
st=list(set(out))
if '.' in st:
    st.remove('.')
if len(st)==0:
    print('Ongoing')
else:
    print(st[0])