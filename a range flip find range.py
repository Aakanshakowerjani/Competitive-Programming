allPaths = []
cnt=[]
def findPaths(maze, m, n):
    path = [0 for d in range(m + n - 1)]
    findPathsUtil(maze, m, n, 0, 0, path, 0)
def findPathsUtil(maze, m, n, i, j, path, indx):
    global allPaths
    if i == m - 1:
        for k in range(j, n):
            path[indx + k - j] = maze[i][k]
        cnt.append(path.count('#'))
        allPaths.append(path)
        return cnt
    if j == n - 1:
        for k in range(i, m):
            path[indx + k - i] = maze[k][j]
        cnt.append(path.count('#'))
        allPaths.append(path)
        return cnt
    path[indx] = maze[i][j]
    findPathsUtil(maze, m, n, i + 1, j, path, indx + 1)
    findPathsUtil(maze, m, n, i, j + 1, path, indx + 1)

n,m=map(int,input().split())
maze=[]
for i in range(n):
    s=input()
    l=[]
    for i in s:
        l.append(i)
    maze.append(l)

findPaths(maze, n, m)
print(min(cnt))

