# A word is considered valid if:
# * It contains a minimum of 3 characters.
# * It contains only digits (0-9), and English letters (uppercase and lowercase).
# * It includes at least one vowel.
# * It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.
# Notes:
# * 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# * A consonant is an English letter that is not a vowel.
#  
# Example 1:
# Input: word = "234Adas"
# Output: true


def valid_word(st:str):
    v = "AEIOUaeiou"
    consonant = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    allowed = v + consonant +'0123456789'
    print(allowed)
    if len(st) <3:
        return False
    isvowel = False
    isconsonant = False
    # isallowed = False
    for i in st:
        if i in v:
            isvowel = True
        if i in consonant:
            isconsonant = True
        if i not in allowed:
            return False


    return isvowel and isconsonant

ip = "234Adas"
op = valid_word(ip)
print(op)


