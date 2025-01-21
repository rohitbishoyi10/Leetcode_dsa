# def prepix(arr:list):
#     ls = arr[0]
#
#     for i in arr[1:]:
#         m = min(i,ls)
#         ln = len(m)
#         if i[:ln] == ls[:ln]:
#             ls = i[:ln]
#
#
#     return ls
#
# a = ["rohit","rohi","s","ro","sss"]
# re = prepix(a)
# print(re)

def find_prefix(arr:list):
    ls = arr[0]
    for i in arr[1:]:
        while not i.startswith(ls):
            ls = ls[:-1]

    return ls

a = ["rohit","rohi","r"]
re = find_prefix(a)
print(re)
