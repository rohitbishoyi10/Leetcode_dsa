# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


# def squares_of_sorted_array(arr):
#     l =0
#     r = len(arr)-1
#     res = []
#
#     while l<=r:
#         if abs(arr[l])>abs(arr[r]):
#             res.append(arr[l]**2)
#             l+=1
#         else:
#             res.append(arr[r]**2)
#             r-=1
#
#     res.reverse()
#     return res
#
# ip = [8,2,7,4,6,5]
# op = squares_of_sorted_array(ip)
# print(op)

#
# def sooort(arr):
#     l=0
#     r=len(arr)-1
#     rs = []
#     while l<=r:
#         if arr[l]>arr[r]:
#             rs.append(arr[l])
#             l+=1
#         else:
#             rs.append(arr[r])
#             r-=1
#     return rs
#
#
# ip = [3,4,5,1,0,9,2]
# op = sooort(ip)
# print(op)

