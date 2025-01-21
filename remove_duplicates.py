# def remove_duplicate_from_arr(arr:list):
#     nd = dict()
#     nl = []
#     for i in arr:
#         if i in nd.keys():
#             nd[i] = nd[i] + 1
#         else:
#             nd[i] = 1
#     for i,j in nd.items():
#         if j==1:
#             nl.append(i)
#
#     return nl
#
# ar = [1,2,2,3,3,4,5,6,7,8]
# re = remove_duplicate_from_arr(ar)
# print(re)

# def remove_duplicate(arr):
#     dct = {}
#     na = []
#
#     for i in arr:
#         dct[i] = dct.get(i,0) + 1
#
#         if dct[i]==1:
#             na.append(i)
#     print(dct)
#     return na
#
# ip = [1,2,2,3,3,4,5,6,7,8,6,6,5,5]
# op = remove_duplicate(ip)
# print(op)


#inplace
# def remove_duplicate_inplace(arr):
#     arr.sort()
#     k = 1
#     for i in range(1,len(arr)):
#         if arr[i]!=arr[i-1]:
#             arr[k] = arr[i]
#             k+=1
#     while len(arr)>k:
#         arr.pop()
#     return arr
#
# ip = [1,2,2,3,3,4,5,6,7,8,6,6,5,5]
# op = remove_duplicate_inplace(ip)
# print(op)


#inplacebettersolution

# def remove_duplicates_inplace(nums):
#     s = set()
#     count = 0
#     for i in nums:
#         if i not in s:
#             s.add(i)
#             nums[count] = i
#             count+=1
#     while len(nums)>count:
#         nums.pop()
#     return nums
#
# nums = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 6, 6, 5, 5,23,21,20,11,11]
# result = remove_duplicates_inplace(nums)
# print(result)
