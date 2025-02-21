# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions


# def max_sum_in_subarray(arr,k):
#     s = set()
#     curr_sum = 0
#     max_sum = -1
#     for i in range(len(arr)):
#         s.add(arr[i])
#         curr_sum = curr_sum + arr[i]
#
#         if len(s)>k:
#             s.remove(arr[i-k])
#             curr_sum = curr_sum - arr[i-k]
#         if len(s) == k and i>=k-1:
#             max_sum = max(curr_sum,max_sum)
#
#     return max_sum
def maximumSubarraySum(nums, k):
    if len(nums)<k:
        return False
    l = 0
    cur_sum = 0
    max_sum = 0
    s = set()
    na = 0
    for i in range(len(nums)):
        while nums[i] in s:
            s.remove(nums[l])
            cur_sum = cur_sum - nums[l]
            l+=1
        s.add(nums[i])
        cur_sum = cur_sum + nums[i]

        if i-l+1 == k:
            if cur_sum>max_sum:
                max_sum = cur_sum
                na = nums[l:i+1]

            # s.remove(nums[l])
            cur_sum = cur_sum - nums[l]
            l+=1
    return max_sum,na
ip =  [1,5,4,2,9,9,9,9,8,7,9]
op = maximumSubarraySum(ip,3)
print(op)




