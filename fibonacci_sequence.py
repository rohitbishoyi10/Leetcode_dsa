def fibo_seq(no):
    if no == 0 :
        return 0
    elif no == 1 or no == 2:
        return 1

    fibo =  fibo_seq(no-1) + fibo_seq(no-2)
    return fibo

for i in range(10):
    re = fibo_seq(i)
    print(re)