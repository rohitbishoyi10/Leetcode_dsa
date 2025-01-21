#ip = aaabbccaa
#op = 3a2b2c2a

#below solution fails because if same char reapets after a different one aaabbaa
# def num_count(st:str):
#     d = dict()
#     ns = ""
#     for i in st:
#         if i in d.keys():
#             d[i] = d[i] + 1
#         else:
#             d[i] = 1
#     for i,j in d.items():
#         ns = ns + str(j) + str(i)
#     return ns
#
# ip  = "aaabbccaa"
# op = num_count(ip)
# print(op)

def num_count(st):
    ns = ""
    count = 1
    for i in range(1,len(st)):
        if st[i] == st[i-1]:
            count+=1
        else:
            ns = ns + str(count) + st[i-1]
            count=1
    ns = ns + str(count) + st[-1]
    return ns

ip =  "aaabbccde"
op = num_count(ip)
print(op)


