#sort dict keys
def dict_sorting(dct):
    lst = list(sorted(dct.keys()))
    nd = dict()
    for i in lst:
        for k in dct.values():
            if dct[i] == k:
                nd[i] = k
    return nd

dct = {2:"a",7:"a",3:"c",4:"d"}
re = dict_sorting(dct)
print(re)
