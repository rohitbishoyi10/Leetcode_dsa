def move_num(arr):
    i = 0
    j = len(arr)-1
    k = 0

    while i<=j:
        if arr[i] <0:
            i+=1
        elif arr[j]>0:
            j-=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return arr

ip = [1,2,3,4,-1,-2,-3,5,6]
op = move_num(ip)
print(op)