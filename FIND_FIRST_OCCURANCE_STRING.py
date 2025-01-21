# Example 1:
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
# #

def find_first_occcurance(st:str,s1):
    l1 = len(st)
    l2 = len(s1)
    for i in range(l1):
        if st[i:l2+i] == s1:
            return i
    return -1


ip = "ssssapbutsad"
ip2 = "sad"
op = find_first_occcurance(ip,ip2)
print(op)
