# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from collections import Counter


def find_all_anagram_in_a_string(st1,st2):
    if len(st1)<len(st2):
        return False

    count_s2 = Counter(st2)
    count_s1 = Counter()
    res = []
    l = 0

    for i in range(len(st1)):
        count_s1[st1[i]] = count_s1[st1[i]] +1

        if i>=len(st2):
            if count_s1[st1[i-len(st2)]] == 1:
                del count_s1[st1[i-len(st2)]]
            else:
                count_s1[st1[i - len(st2)]] -=1
        if count_s2 == count_s1:
            res.append(i-len(st2)+1)
    return res

ip1 ="cbaebabacd"
ip2 = "abc"
op = find_all_anagram_in_a_string(ip1,ip2)
print(op)
