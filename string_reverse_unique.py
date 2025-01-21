# Input - "I am not an String"
#
# Output - "g ni rtS na tonmaI"

def unique_reversal(st):
    ns = ""
    j = 0
    for i in reversed(st):
        if i != " ":
            if st[j]!=" ":
                ns = ns + i
                j+=1
            else:
                ns = ns + " " +i
                j+=2
    return ns

ip = "I am not an String"
op = unique_reversal(ip)
print(op)

