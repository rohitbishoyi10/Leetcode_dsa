# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.




# def majority_elements(arr):
#     n = len(arr)
#     dct = dict()
#
#     for i in arr:
#         if i in dct.keys():
#             dct[i] = dct[i] + 1
#         else:
#             dct[i] = 1
#     for i,j in dct.items():
#         if j>(n//2):
#             return i
#         else:
#             return -1
#
# ip = [2,2,1,1,1,2,2]
# op = majority_elements(ip)
# print(op)

def maj_element(arr):
    dct = {}
    for i in arr:
        dct[i] = dct.get(i,0)+1
        if dct[i] > len(arr)//2:
            return i
    return -1
ip = [2,2,1,1,1,2,2,1,1,1,1,1]
op = maj_element(ip)
print(op)

