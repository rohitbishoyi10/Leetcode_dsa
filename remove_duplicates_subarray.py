# [[1, 2, 2, 3], [4, 5, 5, 6], [7, 7, 8, 8]]

def remove_duplicate_from_subarray(arr):
    nl = []

    for i in arr:
        nl2 = []
        for j in i:
            if j not in nl2:
                nl2.append(j)
        nl.append(nl2)
    return nl
ip = [[1, 2, 2, 3], [4, 5, 5, 6], [7, 7, 8, 8]]
op = remove_duplicate_from_subarray(ip)
print(op)

