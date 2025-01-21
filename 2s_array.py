# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#most inappropriate way
# def two_sum(arr:list,target):
#     nl = []
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#            if arr[i] + arr[j] == target:
#                nl.append(arr[i])
#                nl.append(arr[j])
#     return nl
#
# nums = [2,7,11,15,8,1]
# op = two_sum(nums,9)
# print(op)

#using set

# def target_sum_array(arr,target):
#     s = set()
#     nl = []
#     for i in arr:
#         comp = target - i
#
#         if comp in s:
#             nl.append((comp,i))
#         s.add(i)
#     return nl
#
# ip = [2,7,11,15,8,1]
# op = target_sum_array(ip,9)
# print(op)


# using dict

def two_sum(arr,target):
    map = dict()
    nl = []

    for i,num in enumerate(arr):
        comp = target - num

        if comp in map:
             nl.append([map[comp],i])
        map[num] = i
    return nl

ip =  [2,7,11,15,8,1]
op = two_sum(ip,9)
print(op)




