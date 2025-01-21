# [[1,2,3,4],[2,3,4,5,6,0],[2,7,8,9,7,0]]

def find_duplicate_subarray(arr):
    al = []
    for i in arr[0]:

        flag = True

        for j in arr[1:]:

            if i  not in j:
                flag= False
                break
        if flag:
            al.append(i)
    return al

ip = [[1,2,3,4],[2,3,4,5,6,0],[2,7,8,9,7,0]]
op = find_duplicate_subarray(ip)
print(op)

