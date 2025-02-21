def max_sum_sub_array_unique(arr):
    na = 0
    curr = 0
    maxx =0
    cur_l = 0
    max_l =0
    l = 0
    s = set()
    na = 0

    for i in range(len(arr)):
        while arr[i] in s:
            s.remove(arr[l])
            curr = curr-arr[l]
            l+=1
        s.add(arr[i])
        curr = curr + arr[i]
        cur_l = i-l+1

        if curr>maxx:
            maxx = curr
            na = arr[l:i + 1]
            max_l = cur_l
    return maxx,na,max_l

ip = [6,6,7,8,9,9,7,7,8]
op = max_sum_sub_array_unique(ip)
print(op)


