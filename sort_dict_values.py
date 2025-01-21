def sort_dict_values(dic:dict):
    srt = list(sorted(dic.values()))
    nd = {}

    for i in srt:
        for j in dic.keys():
            if dic[j] == i:
                nd[j] = i
    return nd

dct = {2:"a",7:"a",3:"c",4:"d"}
re = sort_dict_values(dct)
print(re)