def isSquare(num):
    root = int(num ** (1 / 2))
    return ((root * root) == num)


def isCube(num):
    root = int(num ** (1 / 3))
    return ((root * root * root) == num)


def countSC(N):
    count = 0
    for i in range(1, N + 1):
        if isSquare(i):
            count += 1
        elif isCube(i):
            count += 1
    return count
t = int(input())
result = []
test = list(map(int, input().split()))
for i in test:
    result.append(countSC(i))
for i in result:
    print(i)

