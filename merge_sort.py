#merge sort follows the approach of divide and conquer

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    ln = len(arr)-1
    ls = arr[:ln]
    rs = arr[ln:]
    merge_sort(rs)
    merge_sort(ls)
    i = 0
    j = 0
    k = 0
    while i<=len(ls)-1 and j<=len(rs)-1:
        if ls[i]<rs[j]:
            arr[k] = ls[i]
            i+=1
        else:
            arr[k] = rs[j]
            j+=1
        k+=1
    while i<=len(ls)-1:
        arr[k] = ls[i]
        i+=1
        k+=1
    while j<=len(rs)-1:
        arr[k] = rs[j]
        j+=1
        k+=1
    return arr

ar = [3,2,4,5,6,7,8,9,1,0]
re = merge_sort(ar)
print(re)


