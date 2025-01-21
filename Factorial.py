def factorial(no):
    if no == 0:
        return 1
    fact = factorial(no-1) * no

    return fact


re = factorial(10)
print(re)
