# Given a binary array nums, you need to find the maximum number of consecutive 1s in the array, if you can flip at most one 0 to 1.
#
# Key Points:
# Flipping a 0 to 1: You can change one 0 to a 1 in the array, but only once.
# Max Consecutive 1s: You need to find the longest contiguous subarray that contains only 1s after you perform at most one flip.
#
# Input: nums = [1,0,1,1,0,1]
# Output: 4
# Explanation: Flip the second `0` to `1`, and the array becomes: [1,1,1,1,0,1]. The longest consecutive `1`s are 4.

def max_consucative_one_lc487(arr,k):
    l = 0
    cn =0
    mx_num = 0
    zero_count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count+=1
        while zero_count>k:
            if arr[l]==0:
                zero_count-=1
            l+=1
        cn = i-l+1
        mx_num = max(mx_num,cn)
    return mx_num

ip = [1,0,0,1,1,0,1,1,1,0,1]
op = max_consucative_one_lc487(ip,1)
print(op)
