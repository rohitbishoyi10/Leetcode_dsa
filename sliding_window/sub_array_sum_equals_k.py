# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.


from collections import defaultdict
# #
# #
def subarraySum(nums, k):
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1  # Base case: sum 0 occurs once (for the empty subarray)

    current_sum = 0
    result = 0

    for num in nums:
        current_sum += num
        c_sum = current_sum - k

        # Check if there's a subarray sum that equals current_sum - k
        if c_sum in prefix_sum_count:
            result += prefix_sum_count[current_sum - k]

        # Add the current sum to the hashmap
        prefix_sum_count[current_sum] += 1

    return result


ip = [2,4,8,2,4,8]
op = subarraySum(ip,6)
print(op)

# def prefix_sum(arr):
#     na = [1] * len(arr)
#     na[0] = arr[0]
#
#     for i in range(1,len(arr)):
#         na[i] = na[i-1] + arr[i]
#     return na
#
# ip = [10, 20, 10, 5, 15]
# op = prefix_sum(ip)
# print(op)
# from collections import defaultdict
#
#
# def subarraySum(nums, k):
#     # To store the result: a list of tuples where each tuple contains (start_index, end_index)
#     result = []
#
#     # Initialize the prefix sum map with the base case: sum 0 is at index -1
#     prefix_sum_map = defaultdict(list)
#     prefix_sum_map[0].append(-1)  # This handles subarrays starting from index 0
#
#     current_sum = 0
#
#     # Traverse the array
#     for i, num in enumerate(nums):
#         current_sum += num  # Update the current prefix sum
#
#         # Check if there's a previous prefix sum such that current_sum - k = previous_prefix_sum
#         if current_sum - k in prefix_sum_map:
#             # If found, it means we have a subarray summing to k
#             for start_index in prefix_sum_map[current_sum - k]:
#                 result.append((start_index +1, i))  # Store the subarray indices (start, end)
#
#         # Update the map with the current prefix sum and its index
#         prefix_sum_map[current_sum] = [i]
#
#     return result,prefix_sum_map
# ip = [10,10,10]
# op = subarraySum(ip,20)
# print(op)