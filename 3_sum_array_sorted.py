#3 sum array where array is sorted


def triplet_sum_array(arr,target):
    arr.sort()

    for i in range(len(arr)-2):

        l = i+1

        r = len(arr)-1
        required_sum = target - arr[i]
        while l<r:
            sum = arr[l] + arr[r]
            if sum == required_sum:
                return arr[l],arr[r],arr[i]
            if sum > required_sum:
                r = r-1
            else:
                l = l+1
    return -1

ip = [ 2,3,4,5,6,8,9]
op = triplet_sum_array(ip,133)
print(op)
