# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#conventionalway
# def triplet_sum(arr,target):
#     al = []
#     for i in range(len(arr)-2):
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)):
#                 if arr[i] + arr[j] + arr[k] == target:
#                     return arr[i],arr[j],arr[k]
#
#     return -1
#
# ip = [-1,0,1,2,-1,-4]
# op = triplet_sum(ip,0)
# print(op)

#efficient way

def triplet_sum(arr,target):
    # s = set()

    for i in range(len(arr)-2):
        s = set()

        for j in range(i+1,len(arr)):
            comp = target - arr[i] - arr[j]

            if comp in s:
                return arr[i], arr[j] , comp

            s.add(arr[j])
    return -1

ip = [-1,0,1,2,-1,-4]
op = triplet_sum(ip,3)
print(op)

# def triplet_sum(arr,target):
#     closest_sum = 0
#     res = 0
#     arr.sort()
#     for i in range(len(arr)):
#
#         l = i+1
#         r = len(arr)-1
#         sm = target - arr[i]
#         while l<r:
#             summ = arr[l] + arr[r]
#
#             if summ == sm:
#                 return arr[i],arr[l],arr[r]
#             elif summ>sm:
#                 r = r-1
#             else:
#                 l = l+1
#
#     return -1
#
#
# ip =  [-1, 2, 2, 4,8,9,6]
# op = triplet_sum(ip,23)
# print(op)

