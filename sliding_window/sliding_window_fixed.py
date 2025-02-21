def max_average_subarr(arr,k):
    mx = sum(arr[:k])
    max_sum = mx

    for i in range(k,len(arr)):
        mx = mx + arr[i] - arr[i-k]
        max_sum = max(mx,max_sum)
    return max_sum/k


ip1 = [1,12,-5,-6,50,3]
op = max_average_subarr(ip1,4)
print(op)
from programms.general_programme.NEW_PROGRAMS.find_smallest_middle import find_smallest_middle


