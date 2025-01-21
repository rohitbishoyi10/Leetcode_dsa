# 2. Given an array of strings, group the strings that are anagrams of each other.
# Example:
# Input:
# arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Explanation:
# The groups of anagrams are ["eat", "tea", "ate"], ["tan", "nat"], and ["bat"].

def group_anagram(arr):
    dct = dict()
    nl = []
    nl2 = []
    temp = ""
    for i in arr:
        temp = str("".join(sorted(i)))

        if temp in dct.keys():
            dct[temp].append(i)
        else:
            dct[temp] = [i]
        # temp = ""
    for i,j in dct.items():
        nl2.append(j)

    return nl2

a1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
op = group_anagram(a1)
print(op)


