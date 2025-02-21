# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"


def  longest_palandromic_string(st):
    def find_the_stretch(l1,l2):
        while l1>=0 and l2<len(st) and st[l1] == st[l2]:
            l1-=1
            l2+=1
        return st[l1+1:l2]

    final_st = ""

    for i in range(len(st)):
        even = find_the_stretch(i,i)
        odd = find_the_stretch(i,i+1)
        final_st = max(final_st,even,odd,key=len)
    return final_st

ip = "cbbdeccefffff"
op = longest_palandromic_string(ip)
print(op)
