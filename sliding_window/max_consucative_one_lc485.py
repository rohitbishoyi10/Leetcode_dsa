# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#  
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


def consucative_ones(arr):
    num_count = 0
    current = 0
    mx_count = 0
    for i in range(len(arr)):
        if arr[i]==1:
            num_count+=1
            if num_count>mx_count:
                mx_count = num_count
        else:
            num_count = 0
    return mx_count

ip = [1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1]
op = consucative_ones(ip)
print(op)