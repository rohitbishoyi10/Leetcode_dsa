# def two_sum_zero(arr):
#     s = set()
#     for i in arr:
#         comp = -i
#         if comp in s:
#             return comp,i
#         s.add(i)
#     return -1
#
# ip = [1,2,3,4,-2,-1]
# re = two_sum_zero(ip)
# print(re)

def two_sum_index_based(arr):
    dct = {}
    
    for i,j in enumerate(arr):
        comp = -j
        if comp in dct:
            return dct[comp],i
        dct[j] = i
    return -1

ip = [1,2,3,4,-2,-1]
op = two_sum_index_based(ip)
print(op)
