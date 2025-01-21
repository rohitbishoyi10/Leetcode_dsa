# Reverse the letters of every word after the first capital letter, i.e. the words should be at their respective positions but the letters should be reversed after the capital letter.
# Input: Your Name Is Biprabar Sahoo
# Output:  Yruo Nema Is Brabarpi Sooha

def reverse_word_first_cap(st:str):
    words = st.split()
    s = ""
    for i in words:
        if i[0].isupper()==True:
            s = s+ " "+i[0]+i[:0:-1]
        else:
            s = s+ " "+i
    return s.lstrip()

ip = "Your Name Is Biprabar Sahoo"
op = reverse_word_first_cap(ip)
print(op)
