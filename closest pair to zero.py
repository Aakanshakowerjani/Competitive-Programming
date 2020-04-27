"""
from itertools import combinations
n=int(input())
l=list(map(int,input().split()))
comb=combinations(l,2)
m=max(l)
l1=[]
l2=[]
for i in comb:
    if sum(i)==0 :
        l1.append(i)
    elif sum(i)<m:
        m=sum(i)
        l2=[]
        l2.append(i)
    elif sum(i)==m:
        l2.append(i)
print(l1)
print(l2)
if len(l1)==0:
    print(l2)
else:
    print(l1)



def partition(arr, si, ei):
    x = arr[ei]
    i = (si - 1)
    for j in range(si,ei):
        if(arr[j] <= x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
    return (i + 1)

def quickSort(arr, si, ei):
    pi = 0
    if(si < ei):
        pi = partition(arr, si, ei)
        quickSort(arr, si, pi - 1)
        quickSort(arr, pi + 1, ei)

def minAbsSumPair(arr, n):
    sum, min_sum = 0, 10**9
    l = 0
    r = n - 1
    min_l = l
    min_r = n - 1
    if(n < 2):
        print("Invalid Input", end = "")
        return
    quickSort(arr, l, r)
    while(l < r):
        sum = arr[l] + arr[r]
        if(abs(sum) < abs(min_sum)):
            min_sum = sum
            min_l = l
            min_r = r
        if(sum < 0):
            l += 1
        else:
            r -= 1
    print(arr[min_l], arr[min_r])

n=int(input())
arr=list(map(int,input().split()))
minAbsSumPair(arr, n)

"""

def partition(arr, si, ei):
   x = arr[ei]
   i = (si - 1)

   for j in range(si,ei):
      if(arr[j] <= x):
         i += 1
         arr[i], arr[j] = arr[j], arr[i]
   arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
   return (i + 1)

# Implementation of Quick Sort
# arr[] --> Array to be sorted
# si --> Starting index
# ei --> Ending index
def quickSort(arr, si, ei):
   pi = 0 # Partitioning index */
   if(si < ei):
      pi = partition(arr, si, ei)
      quickSort(arr, si, pi - 1)
      quickSort(arr, pi + 1, ei)

def minAbsSumPair(arr, n):

   # Variables to keep track
   # of current sum and minimum sum
   sum, min_sum = 0, 10**9

   # left and right index variables
   l = 0
   r = n - 1

   # variable to keep track of
   # the left and right pair for min_sum
   min_l = l
   min_r = n - 1

   # Array should have at least two elements*/
   if(n < 2):
      print("Invalid Input", end = "")
      return

   # Sort the elements */
   quickSort(arr, l, r)

   while(l < r):
      sum = arr[l] + arr[r]

      # If abs(sum) is less
      # then update the result items
      if(abs(sum) < abs(min_sum)):
         min_sum = sum
         min_l = l
         min_r = r
      if(sum < 0):
         l += 1
      else:
         r -= 1

   print(arr[min_l], arr[min_r])

# Driver Code
n = int(input())
arr = list(map(int,input().split()))

minAbsSumPair(arr, n)