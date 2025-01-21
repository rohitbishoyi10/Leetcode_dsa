def balanced_brace(st):
    while True:
        if  "[]" in st:
            st = st.replace("[]","")
        elif "{}" in st:
            st = st.replace("{}","")
        else:
            return not st

ip = "[]"
op = balanced_brace(ip)
print(op)
