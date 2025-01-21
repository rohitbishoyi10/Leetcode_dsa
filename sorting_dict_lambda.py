#sort dictonary using lambda

dct = {2:"a",7:"a",3:"c",4:"d"}
lst = sorted(dct.keys())
new_dct = dict(sorted(dct.items(),key=lambda x:x[0]))
#for value put 1 instead of 0
print(dict(new_dct))