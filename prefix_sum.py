# Input: arr[] = {10, 20, 10, 5, 15}
# Output: prefixSum[] = {10, 30, 40, 45, 60}


def prefix_sum(arr):
    na = [1]*len(arr)
    na[0] = arr[0]
    for i in range(1,len(arr)):
        na[i] = na[i-1] + arr[i]

    return na

# ip =[10, 20, 10, 5, 15]
# op = prefix_sum(ip)
# print(op)

def sub_array_sum(l,r,arr):
    res = prefix_sum(arr)
    return res[r] - arr[l-1]
ip = [10, 20, 10, 5, 15]
op = sub_array_sum(1,3,ip)
print(op)

