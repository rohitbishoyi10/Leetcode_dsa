def find_smallest_middle(arr):
    mini = max(arr)
    for i in range(1,len(arr)-1):
        if arr[i-1] >arr[i] and arr[i+1]>arr[i]:
            mini = min(mini,arr[i])
    return mini


ip = [1,4,2,3,4,3,6,5,9]
op = find_smallest_middle(ip)
print(op)