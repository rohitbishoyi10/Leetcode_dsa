# Example 1:
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.


def max_num_of_vowels(s1,k):
    vowels = ['a','e','i','o','u']

    cur_count = sum(1 for i in range(k) if s1[i] in vowels)
    max_sum = 0
    chars = 0

    for i in range(k,len(s1)):
        if s1[i] in vowels:
            cur_count+=1
        if s1[i-k] in vowels:
            cur_count-=1

        if cur_count>max_sum:
            max_sum = cur_count
            chars = s1[i-k+1:i+1]

    return max_sum,chars


ip = "xxxxuio"
op = max_num_of_vowels(ip,3)
print(op)
