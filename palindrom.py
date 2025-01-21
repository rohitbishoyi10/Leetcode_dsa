# def palindrom(st):
#     ns = st.strip("%^&*()$#@!.")
#     if ns == "".join(reversed(ns)):
#         print("phrase is palindrom")
#     else:
#         print("no pallindrom")
#
#
#
# re = palindrom("k@aya@k##")

#for int

def pallindrom_int(no):
    if no == int(str(no)[::-1]):
        print("pallindrom")
    else:
        print("not pallindrom")

re = pallindrom_int(3013)
print(re)

