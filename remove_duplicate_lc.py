# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# def remove_duplicate(arr:list):
#     j=1
#     for i in range(1,len(arr)):
#        if arr[i] != arr[i-1]:
#            arr[j] = arr[i]
#            j += 1
#
#     return j ,arr[:j]
#
# ip = [1,1,2,2,3,5,5,6,9,9]
# op = remove_duplicate(ip)
# print(op)
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3
# respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
def remove_duplicate(arr):
    j = 2
    count = 1
    for i in range(2,len(arr)):
        if arr[i]!=arr[j-2] :
            arr[j] = arr[i]
            j+=1
    return arr[:j]

ip =  [0,1,1,1,1,2,3,3]

op = remove_duplicate(ip)
print(op)

