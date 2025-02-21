# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.


def longest_sub_array_after_del_one_element(arr):
    l = 0
    max_length = 0
    zero_count=0
    curr_len = 0

    for i in range(len(arr)):
        if arr[i]==0:
            zero_count+=1
        while zero_count>1:
            if arr[l]==0:
                zero_count-=1
            l+=1
        curr_len = i-l
        if curr_len>max_length:
            max_length = curr_len
    return max_length

ip = [0,1,1,1,0,1,1,0,1]
op = longest_sub_array_after_del_one_element(ip)
print(op)