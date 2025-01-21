# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# def single_number(nums):
#     return 2 * sum(set(nums)) - sum(nums)
#
# # Example usage
# nums = [40, 10, 20, 10, 20]
# print(single_number(nums))  # Output: 4

def single_number(arr):
    num = 0
    for i in arr:
        num^=i
    return num

ip = [2,2,1]
op = single_number(ip)
print(op)
