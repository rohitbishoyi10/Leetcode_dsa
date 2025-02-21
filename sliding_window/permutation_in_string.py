# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


from collections import Counter

# from log_parser.log_parser import count_specific_error


def checkInclusion(s1: str, s2: str):
    if len(s1)>len(s2):
        return False
    s1_count = Counter(s1)

    s2_count = Counter()
    for i in range(len(s2)):
        s2_count[s2[i]] += 1
        if i>=len(s1):
            if s2_count[s2[i-len(s1)]] == 1:
                del s2_count[s2[i-len(s1)]]
            else:
                s2_count[s2[i - len(s1)]] -= 1
        if s1_count == s2_count:
            return True, s1_count,s2_count

    return False

ip1 = "abo"
ip2 = "eeidbaoook"
op = checkInclusion(ip1,ip2)
print(op)