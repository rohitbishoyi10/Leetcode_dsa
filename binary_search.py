#binary search
def bin_search(arr:list,no):
    l = 0
    r = len(arr)-1

    while l<=r:
        mid = (l+r)//2
        if arr[mid] == no:
            return mid
        elif arr[mid]<no:
            l = mid +1
        else:
            r = mid -1
    return -1
a = [1,2,3,4,5,6,7,8]
re = bin_search(a,1)
print(re)