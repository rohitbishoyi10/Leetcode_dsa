#Longest Substring Without Repeating Characters


def longest_substring_wo_repeating_char(st:str):
    s =set()
    length = 0
    l = 0
    for r in range(len(st)):
        while st[r] in s:
            s.remove(st[l])
            l+=1
        s.add(st[r])
        length = max((r-l)+1,length)
    return length

ip = "pwwkew"
op = longest_substring_wo_repeating_char(ip)
print(op)
