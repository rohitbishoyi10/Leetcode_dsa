#move negative int to left using new array

def move_array_left(arr):
    na = []
    a = 0
    for i in arr:
        if i <0:
            na.insert(a,i)
            a+=1
        else:
            na.append(i)
    return na

ar = [1,2,-1,-2,5,6,-10]
re = move_array_left(ar)
print(re)