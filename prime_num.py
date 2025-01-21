def prime_num(no):
    flag = False
    if no==0 or no ==1:
        return False
    else:
        # flag = False
        for i in range(2,no):
            if no%i ==0:
                flag = True
                break

        if flag:
            return False
        else:
            return True
op = prime_num(97)
print(op)
# for i in range(1,100):
#     op = prime_num(i)
#     if op == True:
#         print(i)

