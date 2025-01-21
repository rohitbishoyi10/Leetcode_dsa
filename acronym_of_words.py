# Given an array of strings words and a string s, determine if s is an acronym of words.
#
# The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].
#
# Return true if s is an acronym of words, and false otherwise.

# Example 1:
#
# Input: words = ["alice","bob","charlie"], s = "abc"
# Output: true
# Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym.
# Example 2:
#
# Input: words = ["an","apple"], s = "a"
# Output: false
# Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively.
# The acronym formed by concatenating these characters is "aa".
# Hence, s = "a" is not the acronym.
def acronym_of_words(st:list,word:str):
    if len(word)!=len(st):
        return False
    count = 0
    for i in st:
        if i[0]!=word[count]:
            return False
        count+=1
    return True

ip =  ["alice","bob","charlie"]
ip2 = ["an","apple"]
ip3 = ["never","gonna","give","up","on","you"]
op = acronym_of_words(ip3,"ngguoy")
print(op)