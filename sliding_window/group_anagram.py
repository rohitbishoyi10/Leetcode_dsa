# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# * There is no string in strs that can be rearranged to form "bat".
# * The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# * The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from collections import defaultdict


# def group_anagram(arr):
#     hm = dict()
#     nl = []
#     for i in arr:
#         ns ="".join(sorted(i))
#         # ns = "".join(sorted_string)
#
#         if ns in hm:
#             hm[ns] = hm[ns] + [i]
#         else:
#             hm[ns] = [i]
#     for i,j in hm.items():
#         nl.append(j)
#     return nl
#
# ip = ["eat","tea","tan","ate","nat","bat"]
# op = group_anagram(ip)
# print(op)

def group_anagram(arr):
    def_dict = defaultdict(list)
    for i in arr:
        count =[0] * 26
        for c in i:
            count[ord(c) - ord('a')] +=1
        key = tuple(count)
        def_dict[key].append(i)
    return def_dict.values()

ip = ["eat","tea","tan","ate","nat","bat"]
op = group_anagram(ip)
print(op)
