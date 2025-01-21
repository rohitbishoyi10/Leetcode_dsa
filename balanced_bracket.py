def baclnced_bracket(st):
    al = []
    for i in st:
        if i in "{[(":
            al.append(i)
        else:
            if not al:
                return False
            p = al.pop()
            if i == "}":
                if p!="{":
                    return False
            if i == "]":
                if p!="[":
                    return False
            if i == ")":
                if p!="(":
                    return False
    if al:
        return False
    return True

ip = "{[]}"
op = baclnced_bracket(ip)
print(op)
