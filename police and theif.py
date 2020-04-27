def polth(arr, n, k):
    i = 0
    l = 0
    r = 0
    res = 0
    thi = []
    pol = []

    # store indices in list
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1
    while l < len(thi) and r < len(pol):

        # can be caught
        if (abs(thi[l] - pol[r]) <= k):
            res += 1
            l += 1
            r += 1

        # increment the minimum index
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1

    return res


t=int(input())
while t:
    t-=1
    n,k=map(int,input().split())
    c=0
    for i in range(n):
        l=list(map(str,input().split()))
        c+=polth(l,len(l),k)
    print(c)