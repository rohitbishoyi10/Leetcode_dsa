def longest_repeatative_in_a_string(st:str):
    ns = ""
    count = 1
    mc = 0
    ms = ""

    for i in range(1,len(st)):
        if st[i]==st[i-1]:
            count+=1
            ns = ns + st[i]
            if count>mc:
                mc=count
                ms = ns
        else:
            count=1
            ns = st[i]
    return mc,ms

ip = "aabbbbbbbbccccccccccccc"
op = longest_repeatative_in_a_string(ip)
print(op)
