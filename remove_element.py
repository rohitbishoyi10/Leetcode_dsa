# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of
# nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from test_100.largg import nth_largest


# def remove_element(arr,val):
#     l = 0
#     n = 0
#     while l<len(arr):
#         if arr[l] == val:
#             arr.remove(val)
#             n+=1
#         else:
#             l+=1
#     return arr,n
#
# ip = [0,1,2,2,3,0,4,2]
# op = remove_element(ip,2)
# print(op)

def remove_element(arr,k):
    n = 0

    for i in range(len(arr)):
        if arr[i]!=k:
            n+=1
    return n


ip =  [0,1,2,2,3,0,4,2]
op = remove_element(ip,2)
print(op)