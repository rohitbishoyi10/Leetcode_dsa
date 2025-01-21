# You are given an unsorted array of integers and two integers, r1 and r2,
# which represent the inclusive range.Your task is to count the number of elements in the array
# that fall within this range, including the boundaries.
#
# 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:
# 𝐈𝐧𝐩𝐮𝐭:
# Array = [1, 3, 5, 2]
# r1 = 1
# r2 = 5
# Output:
# 4
#
# 𝐄𝐱𝐩𝐥𝐚𝐧𝐚𝐭𝐢𝐨𝐧:
# All elements in the array (1, 3, 5, 2) are within the range [1, 5], so the output is 4.

def find_number_range(arr,n1,n2):
    arr.sort()
    count=0
    for i in arr:
        if i>=n1 and i<=n2:
            count+=1
    return count

ip = [1, 3, 5, 2,12,14]
op = find_number_range(ip,1,15)
print(op)