# Given a sorted array of distinct positive integers arr[]
# and integer k, the task is to find the kth positive number that is missing from arr[].
# Input: arr[] = [2, 3, 4, 7, 11], k = 5
# Output: 9
# Explanation: Missing are 1, 5, 6, 8, 9, 10, … and 5th missing number is 9.
#
#
# Input: arr[] = [1, 2, 3], k = 2
# Output: 5
# Explanation: Missing are 4, 5, 6…. and 2nd missing number is 5.
#
#
# Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
# Output: 2
# Explanation: Missing are 1, 2, 4, 6, 7, 8, 13,…  and 2nd missing number is 2.

# Python Program to find Kth missing positive number
# using Hash Set

# def kthMissing(arr, k):
#     s = set(arr)
#     count = 0
#     mis = 0
#     while count<k:
#         mis+=1
#         if mis not in s:
#             count+=1
#     return mis
#
# ip = [4, 7, 9, 10]
# op = kthMissing(ip,5)
# print(op)

# Python Program to find Kth missing positive number
# using Binary Search

# Function to find the k-th missing positive number
def kthMissing_unsorted_array(arr, k):
    mn = min(arr)
    mx = max(arr)
    s = set(arr)
    nl = []
    for i in range(mn,mx):
        if i not in s:
            nl.append(i)
    print(nl)
    if k<=len(nl):
        return nl[k-1]
    else:
        return len(arr) + (k-len(nl))

arr = [3, 7, 1, 9, 5]
k =4
re = kthMissing_unsorted_array(arr,k)
print(re)