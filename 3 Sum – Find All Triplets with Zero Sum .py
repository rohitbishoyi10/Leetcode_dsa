# def three_sum_set(nums):
#     nums.sort()  # Step 1: Sort the array
#     triplets = set()  # To store unique triplets
#     n = len(nums)
#
#     for i in range(n - 2):  # Fix the first element
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue  # Skip duplicates for the first element
#
#         seen = set()  # To find pairs
#         # target = -nums[i]
#         for j in range(i + 1, n):  # Traverse the rest of the array
#             complement = -nums[i] - nums[j]
#             if complement in seen:  # Found a valid pair
#                 triplets.add((nums[i], complement, nums[j]))
#             seen.add(nums[j])  # Add the current number to the set
#
#     return [list(triplet) for triplet in triplets]  # Convert to a list of lists
#
#
#
#
# ip = [3,4,5,-2,-1,9,8,4]
# re = three_sum_set(ip)
# print(re)

#using 2 pointers

def sum_find_trilets_zero_sum(arr):
    arr.sort()
    na = []
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            continue
        l = i+1
        r = len(arr)-1
        while l<r:
            suum = arr[i] +arr[l] +arr[r]
            if suum == 0:
                na.append((arr[i] , arr[l] ,arr[r]))
                l+=1
                r-=1
            elif suum>0:
                r = r-1
            else:
                l=l-1
    return na


ip =  [3,4,5,-2,-1,9,8,4,0,1]
op = sum_find_trilets_zero_sum(ip)
print(op)