#2s array where array is sorted
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

def two_sum(arr,target):
    l = 0
    ln = len(arr)
    r = len(arr)-1

    while l<r:
        sum = arr[l] + arr[r]
        if target == sum:
            return arr[l],arr[r]
        if sum>target:
            r=r-1
        else:
            l=l+1

    return -1

ip = [2,7,11,15]
op = two_sum(ip,9)
print(op)