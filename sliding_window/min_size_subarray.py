# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
from turtledemo.penrose import inflatedart


def min_size_array(arr,target):
    l = 0
    sum = 0
    diff = float('inf')
    for i in range(len(arr)):
        sum = sum+arr[i]
        while sum>=target:
            diff = min(diff,i-l+1)
            sum= sum-arr[l]
            l+=1
    return  diff if diff!= float('inf') else None
ip =  [2,3,1,2,4,3]
op = min_size_array(ip,7)
print(op)
