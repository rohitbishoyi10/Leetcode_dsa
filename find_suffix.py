def find_suffix(lst):
    first = lst[0]
    for i in lst[1:]:
        while not i.endswith(first):
            first = first[1:]
    return first

ip = ["rohit","hit","t"]
print(ip)
op = find_suffix(ip)
print(op)
