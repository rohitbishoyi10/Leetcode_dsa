# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


def subarraysDivByK(nums, k):
    from collections import defaultdict


from collections import defaultdict


def subarraysDivByK(nums, k):
    # To store the frequency of each remainder of prefix sums modulo k
    prefix_sum_map = defaultdict(int)

    # Initial state: prefix sum of 0, i.e., no elements considered yet
    prefix_sum_map[0] = 1

    current_sum = 0
    count = 0

    for num in nums:
        # Update the current sum (prefix sum)
        current_sum += num

        # Find the remainder when dividing by k
        remainder = current_sum % k

        # Handle negative remainders (Python's mod can give negative results)
        if remainder < 0:
            remainder += k

        # If this remainder has been seen before, it means there are subarrays
        # whose sum is divisible by k
        if remainder in prefix_sum_map:
            count += prefix_sum_map[remainder]


        # Update the map with the current remainder
        prefix_sum_map[remainder] += 1

    return count


nums = [4,5,0,-2,-3,1]
k = 5
op = subarraysDivByK(nums,k)
print(op)
