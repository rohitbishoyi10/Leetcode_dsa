#move negative intiger to right side

# def mov_int_right_side(arr:list):
#     na = []
#     a = 0
#     for i in arr:
#         if i <0:
#             na.append(i)
#         else:
#             na.insert(a,i)
#             a+=1
#     return na
#
# a1 = [2,3,-4,-7,9,-1]
# re = mov_int_right_side(a1)
# print(re)

#move negative int to right side
def mov_int_right_inplace(arr):
    a =-1
    i = len(arr)-1
    n = 1
    l = len(arr)-n
    while i>=0:
        l = len(arr) - n
        if arr[i]<0:
            num = arr.pop(i)
            arr.insert(l,num)
            n+=1
        i-=1
    return arr

a1 = [2,3,-4,-7,9,-1]
re = mov_int_right_inplace(a1)
print(re)

