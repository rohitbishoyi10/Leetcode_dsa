def contains_duplicate(arr):
    s = set()
    nl = []

    for i in arr:
        if i in s:
            nl.append(i)
        else:
            s.add(i)
    return nl

ip = [1,2,2,3,4,5,6,6,7,8,9,9,9]
op =contains_duplicate(ip)
print(op)