# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#  
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
# Input: arr = [1,2]
# Output: false
# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

def unique_occurances(arr):
    nd = dict()
    s = set()
    for i in arr:
        nd[i] = nd.get(i,0) +1
    print(nd)
    for j in nd.values():
        if j in s:
            return False
        else:
            s.add(j)
    return True

ip =   [-3,0,1,-3,1,1,1,-3,10,0]
op = unique_occurances(ip)
print(op)
