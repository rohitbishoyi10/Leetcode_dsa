

def three_sum_less_than_target(arr,target):
    arr.sort()
    maxx = 0
    for i in range(len(arr)):
        l = i +1
        r = len(arr)-1
        while l<r:
            suum = arr[l] + arr[r] + arr[i]
            if suum < target:
                maxx = suum
                l+=1
            else:
                r-=1
    return maxx

ip = [3,2,4,5,6,7]
op = three_sum_less_than_target(ip,16)
print(op)
