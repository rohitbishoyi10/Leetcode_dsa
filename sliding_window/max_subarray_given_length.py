def max_average_sub_array_k_length(arr,k):
    cur_sum = 0
    max_sum = 0
    l = 0
    s = set()
    cur_len = 0
    max_len = 0

    for i in range(len(arr)):
        cur_sum = cur_sum+arr[i]
        cur_len = i-l+1

        if cur_len == k:
            if cur_sum >max_sum:
                max_sum = cur_sum
                max_len = arr[l:i + 1]

            cur_sum = cur_sum-arr[l]
            l+=1
    return max_sum/k,max_len,max_sum


ip = [1, 12, -5, -6, 50, 3]
op = max_average_sub_array_k_length(ip,4)
print(op)
