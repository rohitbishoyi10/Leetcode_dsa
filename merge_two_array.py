# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
# that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#  
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# def merge_two_sorted_array(arr1,arr2):
#     na = []
#     i=0
#     j=0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i] <arr2[j]:
#             na.append(arr1[i])
#             i+=1
#         elif arr2[j]>arr1[i] :
#             na.append(arr2[j])
#             j+=1
#         else:
#             na.append(arr1[i])
#             na.append(arr2[j])
#             i+=1
#             j+=1
#     while i < len(arr1) :
#             na.append(arr1[i])
#             i += 1
#
#
#     while j<len(arr2):
#             na.append(arr2[j])
#             j+=1
#
#
#
#     return na
#
#
#
# nums1 = [1,2,3,0,0,0,3,4,5]
# nums2 = [2,5,6]
# re = merge_two_sorted_array(nums1,nums2)
# print(re)

# def merge_two_sorted_array(arr1,arr2):
#     for i in arr2:
#         arr1.append(i)
#
#     while True:
#         if 0 in arr1:
#             arr1.remove(0)
#         else:
#             break
#
#     arr1.sort()
#     return arr1
#
# nums1 = [1,2,3,0,0,0,3,4,5]
# nums2 = [2,5,6]
# re = merge_two_sorted_array(nums1,nums2)
# print(re)
# def merge_two_sorted_array(arr1,arr2,l1,l2):
#     m = l1-1
#     n = l2-1
#     for i in range(l1+l2-1,-1,-1):
#         if m<0:
#             arr1[i] = arr2[n]
#             n-=1
#         elif n<0:
#             break
#         elif arr1[m]>arr2[n]:
#             arr1[i] = arr1[m]
#             m-=1
#         else:
#             arr1[i] = arr2[n]
#             n-=1
#     return arr1
#
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# re = merge_two_sorted_array(nums1,nums2,3,3)
# print(re)

# def merge_sorted(arr1,arr2,m,n):
#     for i in range(m):
#         arr1[m+i] = arr2[i]
#     arr1.sort()
#     return arr1
#
#
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# op = merge_sorted(nums1,nums2,3,3)
# print(op)


