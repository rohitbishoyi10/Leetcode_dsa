#
#
#
# You are given an array of integers called nums. Your task is to create a new array result such that each element at index i of the result is the product of all the elements in nums except nums[i].
# Important:
# You cannot use division in this problem.
# Try to solve the problem in O(n) time complexity.
# 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:
# 𝐈𝐧𝐩𝐮𝐭:
# nums = [1, 2, 3, 4]
# Output:
# result = [24, 12, 8, 6]
# 𝐄𝐱𝐩𝐥𝐚𝐧𝐚𝐭𝐢𝐨𝐧:
# The product of all elements except the one at index 0 is 2 * 3 * 4 = 24.
# The product of all elements except the one at index 1 is 1 * 3 * 4 = 12.
# The product of all elements except the one at index 2 is 1 * 2 * 4 = 8.
# The product of all elements except the one at index 3 is 1 * 2 * 3 = 6.

# def product_all_elements(arr):
#     n = len(arr)
#     na = [1] * n
#     p = 1
#     for i in range(n):
#         for j in range(n):
#             if i!=j:
#                 na[i] = na[i] *arr[j]
#     return na
# ip =  [1, 2, 3, 4]
# op = product_all_elements(ip)
# print(op)

# def product_of_elements(arr:list):
#     n = len(arr)
#     na = [1]*n
#     left_product = 1
#     for i in range(n):
#         na[i] = left_product
#         left_product*=arr[i]
#     right_product = 1
#     for i in range(n-1,-1,-1):
#         na[i]*=right_product
#         right_product*=arr[i]
#     return na
# ip =  [1, 2, 3, 4]
# re = product_of_elements(ip)
# print(re)

def product_all_elemnt(arr):
    na = [1] * len(arr)
    product_left = 1
    for i in range(len(arr)):
        na[i] = product_left
        product_left*=arr[i]
    right_product = 1
    for j in range(len(arr)-1,-1,-1):
        na[j]*=right_product
        right_product*=arr[j]

    return na

ip =  [1, 2, 3, 4]
op = product_all_elemnt(ip)
print(op)