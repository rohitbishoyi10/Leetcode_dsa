from idlelib.pyparse import trans


# def top_k_repeat_array(arr,k):
#     dct = dict()
#     for i in arr:
#         if i in dct.keys():
#             dct[i] = dct[i] + 1
#         else:
#             dct[i] = 1
#     nl = sorted(dct.items(),key=lambda x:x[1],reverse=True)
#     nl2 = nl[:k]
#     ll2 =  [i for i,j in nl2 if j==k]
#     return ll2
#
#
# ip = [1,1,2,2,3,40,40,40]
# op = top_k_repeat_array(ip,2)
# print(op)


def top_k_reapeat_elements(arr,k):
    dct = dict()
    for i in arr:
        dct[i] = dct.get(i,0) +1
    nl = sorted(dct.items(),key=lambda x:x[1],reverse=True)
    nl2 = nl[:k]
    nl3 = [i for i in nl2]

    return nl3

ip = [1,1,2,2,3,40,40,40]
op = top_k_reapeat_elements(ip,9)
print(op)
