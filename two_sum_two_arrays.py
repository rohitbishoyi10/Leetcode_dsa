# Find all pairs with a given sum in two unsorted arrays


#conventional way
# def two_sum_two_arrays(arr1,arr2,target):
#     l1 = len(arr1)
#     l2 = len(arr2)
#     res = []
#
#     for i in range(l1):
#         for j in range(l2):
#             if arr1[i] + arr2[j] == target:
#                 res.append((arr1[i],arr2[j]))
#     return res
#
# a1 = [-1, -2, 4, -6, 5, 7]
# a2 = [6, 3, 4, 0]
# re = two_sum_two_arrays(a1,a2,8)
# print(re)


#using set//efficient way

# def two_sum_two_array(arr1,arr2,target):
#     l1 = len(arr1)
#     l2 = len(arr2)
#     s = set(arr1)
#
#     for i in range(l2):
#         compliment = target - arr2[i]
#         if compliment in s:
#             return compliment, arr2[i]
#
#     return -1
#
# a1 = [-1, -2, 4, -6, 5, 7]
# a2 = [6, 3, 4, 0]
# re = two_sum_two_array(a1,a2,8)
# print(re)


#retrive the index
# def two_sum_index_based(arr1,arr2,target):
#     l1 = len(arr1)
#     l2 = len(arr2)
#     dct = {}
#     for m,n in enumerate(arr1):
#         dct[n] = m
#     print(dct)
#
#     for j in range(l2):
#         compliment = target - arr2[j]
#         if compliment in dct:
#             return dct[compliment],j
#     return -1
#
# a1 = [-1, -2, 4, -6, 5, 7]
# a2 = [6, 3, 4, 0]

# re = two_sum_index_based(a1,a2,8)
# print(re)



