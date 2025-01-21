# def find_duplicate(arr:list):
#     nd = dict()
#     nl = []
#     for i in arr:
#         if i in nd.keys():
#             nd[i] = nd[i] + 1
#         else:
#             nd[i] = 1
#     for j,k in nd.items():
#         if k>1:
#             nl.append(j)
#     return nl
#
# al = [2,2,3,3,3,4,5,6,7,8]
# re= find_duplicate(al)
# print(re)
from programms.general_programme.count_number_range import find_number_range


def find_duplicate(arr):
    arr.sort()
    j = 1
    na = []
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            na.append(arr[i])
    return na

ip = [2,2,3,3,3,4,5,6,7,8,4]
op = find_duplicate(ip)
print(op)