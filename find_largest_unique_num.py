# Given an array of integers, find the largest number that does not have any duplicates in the array.
# Example:
# Input:
# arr = [4, 3, 2, 7, 3, 4, 8]
# Output:
# 8
# Explanation:
# The unique numbers are [2, 7, 8], and the largest among them is 8.

def largest_unique(arr):
    dct = dict()
    for i in arr:
        if i in dct.keys():
            dct[i] = dct[i] + 1
        else:
            dct[i] =1
    max = 0
    for i,j in dct.items():
        if j==1 and i>=max:
            max=i
            # nl.append(i)
    # max = 0
    # for k in nl:
    #     if k>=max:
    #         max = k
    return max

ip = [4, 3, 2, 7, 3, 4, 8]
op = largest_unique(ip)
print(op)