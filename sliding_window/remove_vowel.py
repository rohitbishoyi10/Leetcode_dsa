# ip = "programing is fun"
# op = "Prgrmng s fn"


def remove_vowel(ip):
    vowel = ["a","e","i","o","u"]
    ns = ""
    for i in ip:
        if i not in vowel:
            ns = ns + i
    s = ns.split()
    ns2 = ""
    for j in s:
        ns2 = ns2 + " " + j[0].capitalize() + j[1:]
    return ns2.lstrip()
ip = "programing is fun"
op = remove_vowel(ip)
print(op)