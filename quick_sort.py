#adv quick sort using recursive approach

def quick_sort(arr:list):
    if len(arr)<=1:
        return arr
    pvt = arr.pop()
    a1 = []
    a2 = []

    for i in arr:
        if i<pvt:
            a1.append(i)
        else:
            a2.append(i)

    return quick_sort(a1) + [pvt] + quick_sort(a2)

ar = [4,3,5,6,7,8,9,1,2]
re = quick_sort(ar)
print(re)