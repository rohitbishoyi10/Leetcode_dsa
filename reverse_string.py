# def reverse_string(st:str):
#     l = list(st[::-1])
#     ns = "".join(l)
#     return ns
#
# ip = "rohit"
# op = reverse_string(ip)
# print(op)
#different way
def reverse_strr(st:str):
    ns = ""
    for i in st:
        ns = i + ns
    return ns

ip = "rohit"
op = reverse_strr(ip)
print(op)