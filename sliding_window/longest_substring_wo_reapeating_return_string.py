# def longest_substring_without_repeating(s):
#     char_index = {}  # Dictionary to store the last index of each character
#     start = 0  # Left pointer of the sliding window
#     max_length = 0
#     longest_substring = ""  # To store the actual substring
#
#     for end in range(len(s)):
#         if s[end] in char_index and char_index[s[end]] >= start:
#             # Update the start position to avoid repeating characters
#             start = char_index[s[end]] + 1
#
#         # Update the last index of the character
#         char_index[s[end]] = end
#
#         # Calculate the maximum length and update the longest substring
#         current_length = end - start + 1
#         if current_length > max_length:
#             max_length = current_length
#             longest_substring = s[start:end + 1]
#
#     return longest_substring
#
#
# # Example Usage
# s = "abcdabcbb"
# result = longest_substring_without_repeating(s)
# print(result)  # Output: "abc"
# def find_nonreapeat_substring()


# def longest_substring_without_repeat(st:str):
#     dct = dict()
#     start = 0
#     max_l = 0
#     max_st = ""
#     index = []
#     lft = 0
#
#     for i in range(len(st)):
#         if st[i] in dct and dct[st[i]] >=start:
#             start = dct[st[i]] + 1
#         dct[st[i]] = i
#         cl = i-start + 1
#         if cl>max_l:
#             max_l = cl
#             lft = start
#
#     return st[lft:max_l+lft],lft,max_l
#
# ip = "abcdffghnnmm"
# op = longest_substring_without_repeat(ip)
# print(op)

def longest_unique_substring(s):
    # To store the characters in the current window
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0  # Start index of the longest substring
    chars = 0

    for right in range(len(s)):
        # If the character at 'right' is already in the window, shrink from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the new character to the set
        char_set.add(s[right])

        # Update the maximum length of the substring
        if right - left + 1 > max_length:
            max_length = right - left + 1
            chars = s[left:right+1]
            # start_index = left
    return chars

    # Return the longest substring



# Example usage:
s = "abcdbcbzxcvba"
result = longest_unique_substring(s)
print(f"Longest unique substring: {result}")



