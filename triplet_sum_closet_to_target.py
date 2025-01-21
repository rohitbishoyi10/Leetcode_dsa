# Input: arr[] = [-1, 2, 2, 4], target = 4
# Output: 5
# Explanation: All possible triplets

def triplet_sum_closer_totarget(arr,target):
    arr.sort()
    closer = 0
    for i in range(len(arr)):
        if arr[i] ==arr[i-1]:
            continue
        l = i+1
        r = len(arr)-1
        while l<r:
            sum = arr[i] + arr[l] + arr[r]
            if abs(sum-target)<abs(closer-target):
                closer = sum
            elif sum == target:
                return sum
            elif sum<target:
                l=l+1
            else:
                r=r-1
    return closer




ip =  [-1, 2, 2, 4,8,9,6]
ip2 = [-1, 2, 2, 4]
op = triplet_sum_closer_totarget(ip2,4)
print(op)

#different way

# def triplet_sum_closer_totarget(arr,target):
#     arr.sort()
#     res = []
#     closer = 0
#     for i in range(len(arr)):
#         if arr[i] ==arr[i-1]:
#             continue
#         l = i+1
#         r = len(arr)-1
#         while l<r:
#             sum = arr[i] + arr[l] + arr[r]
#             # if abs(sum-target)<abs(closer-target):
#             #     closer = sum
#             # elif sum == target:
#             #     return sum
#             if sum<target:
#                 l=l+1
#             elif sum>target:
#                 r=r-1
#             else:
#                 res.append([arr[l],arr[r].arr[i]])
#                 l+=1
#                 while arr[l] == arr[l-1] and l<r:
#                     l+=1
#
#
#     return res
#
#
#
#
# ip =  [-1, 2, 2, 4,8,9,6]
# ip2 = [-1, 2, 2, 4]
# op = triplet_sum_closer_totarget(ip2,4)
# print(op)