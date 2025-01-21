def reverse_words(st):
    # s = str(st)
    # print(s)
    # sp = s.split()
    ns = []
    for i in st:
        rev = i[::-1]
        ns.append(rev)
    # nss = " ".join(ns)
    return ns

# ip = "rohit kumar bishoyi"
ip = ["rohit","kumar","bishoyi"]
op = reverse_words(ip)
print(op)

