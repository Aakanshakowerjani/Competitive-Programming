""""
m,n=map(int,input().split())
if m%2==0 and n%2==0:
    print("YES")
elif m%n==0:
    print("YES")
else:
    print("NO")
"""

# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint
def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [-3,4,3,-5,7,-8,5,-5,3,8]
print(maxSubArraySum(a, len(a)))
