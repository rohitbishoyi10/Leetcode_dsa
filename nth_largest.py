# def nth_largest(arr:list,n):
#     arr.sort()
#     l = len(arr)
#     return arr[l-n]
#
#
# ar = [1,3,2,5,4,6]
# re = nth_largest(ar,1)
# print(re)

#differentway

# def nth_largest(arr:list,n):
#
#     na = []
#     i = 0
#     while i<=n:
#         max = 0
#         for j in arr:
#             if j>max:
#                 max=j
#                 # val = max
#         arr.remove(max)
#         na.append(max)
#         i+=1
#
#     return na[n-1]
#
# ip = [2,1,3,5,6,7,9]
# op = nth_largest(ip,3)
# print(op)
#using_quickselect
# def k_th_smallest(arr,k):
#
#     def find_pivot(l,r):
#         i = l
#         pivot = arr[r]
#         for j in range(l,r):
#             if arr[j]>pivot:
#                 arr[i],arr[j] = arr[j],arr[i]
#                 i+=1
#         arr[i],arr[r] = arr[r],arr[i]
#         return i
#     low = 0
#     high = len(arr)-1
#     k = k-1
# #
#     while low <= high:
#         pivot = find_pivot(low,high)
#         if pivot == k:
#             return arr[pivot]
#         elif pivot<k:
#             low = pivot+1
#         else:
#             high = pivot-1
#
# nums = [30, 20, 10, 50, 40]
# k = 1
# re = k_th_smallest(nums,k)
# print(re)
def partition(arr, l, r):
    j=l
    pivot = arr[r]
    for i in range(l, r):
        if arr[i] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j+=1
    arr[j], arr[r] = arr[r], arr[j]
    return j

def kth_largest(arr,k):
    left = 0
    right = len(arr)-1
    target = k-1
    while left<right:
        par = partition(arr, left, right)
        if par == target:
            return arr[par]
        elif par > target:
            right = par-1
        else:
             left = par+1

ip = [1,2,3,4,5,6,7,8,9,100]
op = kth_largest(ip,3)
print(op)




