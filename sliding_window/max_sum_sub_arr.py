# Given an integer array nums, find the
# subarray
#
# with the largest sum, and return its sum.
#  
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


# def max_sum_subarray(arr):
#     total_sum = 0
#     max_count = 0
#     l=0
#     for i in range(len(arr)):
#         total_sum = total_sum + arr[i]
#         max_count = max(max_count,total_sum)
#         if total_sum<0:
#             total_sum = 0
#     return max_count
#
#
# ip =[-2,1,-3,4,-1,2,1,-5,4]
# op = max_sum_subarray(ip)
# print(op)


#using kadesns


# def max_sum_subarray(arr):
#     curr = 0
#     maxx =0
#
#     for i in range(0,len(arr)):
#         curr = max(arr[i],arr[i]+curr)
#         maxx = max(curr,maxx)
#
#     return maxx
#
# ip = [0,-1,-9,4,5,-3,6,1,2,-3,-1,-2]
# op = max_sum_subarray(ip)
# print(op)

#kadensreturn index

def max_sum_subarray(arr):
    l =0
    r =0
    max_sum = 0
    summ = 0
    win = 0

    for i in range(len(arr)):
        if arr[i]>arr[i] + summ:
            summ = arr[i]
            l = i
        else:
            summ = arr[i] + summ

        if summ >max_sum:
            max_sum = summ
            win = arr[l:i+1]
    return win,max_sum

ip = [6,6,7,8,9,9,7,7,8]
op = max_sum_subarray(ip)
print(op)