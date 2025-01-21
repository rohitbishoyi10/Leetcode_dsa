#move negative numbers to left in place
def mov_negative_to_left(arr):
    a = 0
    for i in range(len(arr)):
        if arr[i]<0:
            num = arr.pop(i)
            arr.insert(a,num)
            a+=1
    return arr

a = [1,2,-1,-2,7,8,-9]
re = mov_negative_to_left(a)
print(re)