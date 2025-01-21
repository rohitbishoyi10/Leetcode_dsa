#  Given a string s consisting of words and spaces, return the length of the last word in the string.
# Input: "luffy is still joyboy"
# Edge Case: "   fly me   to   the moon  "

def return_length(st:str):
    sp = st.split()
    # print(sp)
    l = len(sp[-1])
    return l

ip = "   fly me   to   the   "
op = return_length(ip)
print(op)