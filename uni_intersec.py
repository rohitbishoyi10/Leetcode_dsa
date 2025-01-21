# a = [1,2,3,4,5,6,7,8]
# b = [6,7,8,9,10]
#
# def uni(ls,lss):
#     nl = []
#     int = []
#     for i in ls:
#         nl.append(i)
#     for j in lss:
#         if j  not in nl:
#             nl.append(j)
#     for k in lss:
#         if k  in ls:
#             int.append(k)
#     return nl,int
#
# re = uni(a,b)
# print(re)
#different way
def uni_intersec(arr1,arr2):
    uni = []
    inter_sec = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            uni.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            uni.append(arr2[j])
            j+=1
        else:
            uni.append(arr1[i])
            inter_sec.append(arr2[j])
            i+=1
            j+=1
    while i<len(arr1):
        uni.append(arr1[i])
        i+=1
    while j<len(arr2):
        uni.append(arr2[j])
        j+=1
    return uni,inter_sec

a = [1,2,3,4,5,6,7,8]
b = [6,7,8,9,10]
re = uni_intersec(a,b)
print(re)

