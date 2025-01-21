# def max_repeating_elemets(arr:list):
#     nd = dict()
#     nl = []
#     for i in arr:
#         if i in nd.keys():
#             nd[i] = nd[i] + 1
#         else:
#             nd[i] = 1
#     mx = max(nd.values())
#     for i,j in nd.items():
#         if j==mx:
#             nl.append(i)
#
#     return nl
#
# ar = [1,2,2,3,3,3,4,5,6,7,8]
# re = max_repeating_elemets(ar)
# print(re)