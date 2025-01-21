def two_sum_closetst_to_target(arr,target):
    closest = 0
    l= 0
    r = len(arr)-1
    while l<r:
        summ = arr[l] + arr[r]
        if abs(summ - target)<abs(closest - target):
            closest = summ
        elif summ == target:
            return summ
        elif summ > target:
            r = r-1
        else:
            l = l+1
    return closest

ip2 = [-1, 2, 2, 4]
re = two_sum_closetst_to_target(ip2,5)
print(re)
