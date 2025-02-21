# Given
# a
# binary
# array
# nums and an
# integer
# k,
# return the
# maximum
# number
# of
# consecutive
# 1
# 's in the array if you can flip at most k 0'
# s.
#
# Example
# 1:
#
# Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
# Output: 6
# Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
# Bolded
# numbers
# were
# flipped
# from
#
# 0
# to
# 1.
# The
# longest
# subarray is underlined.
# Example
# 2:
#
# Input: nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
# Output: 10
# Explanation: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# Bolded
# numbers
# were
# flipped
# from
#
# 0
# to
# 1.
# The
# longest
# subarray is underlined.
#
#
def max_consucative_one(arr,k):
    l=0
    max_l =0
    cl =0
    zero_count =0
    for i in range(len(arr)):
        if arr[i]==0:
            zero_count+=1
        while zero_count>k:
            if arr[l]==0:
                zero_count-=1
            l+=1
        cl = i-l+1
        max_l = max(max_l,cl)
    return max_l

ip = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
op = max_consucative_one(ip,2)
print(op)

