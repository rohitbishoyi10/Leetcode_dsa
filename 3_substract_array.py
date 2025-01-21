# def findTripletWithDifference(nums, target):
#     # Step 1: Create a set for fast lookups
#     num_set = set(nums)
#
#     # Step 2: Iterate through each number as the middle value
#     for mid in nums:
#         # Calculate potential min and max values
#         min_val = mid - target
#         max_val = mid + target
#
#         # Check if both min_val and max_val exist in the set
#         if min_val in num_set and max_val in num_set:
#             # Ensure all three values are distinct
#             if min_val != mid and max_val != mid and min_val != max_val:
#                 return [min_val, mid, max_val]
#
#     return None  # No triplet found
#
#
# # Example usage
# nums = [1, 2, 5, 10, 15]
# target = 5
# result = findTripletWithDifference(nums, target)
# print("Triplet with specified difference:", result)  # Output: [5, 10, 15]


# def three_substract_array(arr,target):
#     arr.sort()
#
#     for i in range(len(arr)-2):
#         l = i+1
#         r = len(arr)-1
#         while l<r:
#             currentdiff = arr[r] - arr[i]
#             if currentdiff == target:
#                 return arr[i],arr[l],arr[r]
#             elif currentdiff>target:
#                 r = r-1
#             else:
#                 l=l+1
#     return -1
#
# ip = [1,2,3,4,5,6,7,8]
# op = three_substract_array(ip,0)
# print(op)

#
def findTripletWithDifference(nums, target):
    nums.sort()  # Step 1: Sort the array
    n = len(nums)

    for i in range(n - 2):  # Fix one number
        left = i + 1
        right = n - 1

        while left < right:  # Step 2: Use two pointers
            current_min = nums[i]
            current_max = nums[right]
            current_diff = current_max - current_min

            if current_diff == target:
                return [nums[i], nums[left], nums[right]]  # Found triplet

            if current_diff < target:
                left += 1  # Increase min by moving left pointer
            else:
                right -= 1  # Decrease max by moving right pointer

    return None  # No triplet found


# Example usage
nums = [1,2,3,4,5,6,7,8]
target = 4
result = findTripletWithDifference(nums, target)
print("Triplet with specified difference:", result)
