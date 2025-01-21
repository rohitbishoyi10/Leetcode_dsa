from test_100.practice123 import find_pre


def find_first_occurance(st):
    nl = list()
    nl2=set()
    count = 0
    for i in st:
        if i not in nl:
            nl.append(i)
        else:
            nl2.add(i)
    ll = list(nl2)
    print(ll)
    if len(ll)>1:
        return nl[1]



ip = "roohhiiiit"
op = find_first_occurance(ip)
print(op)