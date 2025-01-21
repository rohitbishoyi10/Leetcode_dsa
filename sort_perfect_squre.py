# 3.{7, 64, 9, 13, 1, 4, 33, 25, 98} -
# Sort perfect squares in an array at their relative positions after doing their square root
import math


def is_perfect_squre(no):
     sq_rt = math.isqrt(no)
     return sq_rt * sq_rt == no

def find_perfect_squre(arr):
    nl = [math.isqrt(i) for i in arr if is_perfect_squre(i)]
    nl.sort()
    na = []
    count = 0
    for i in arr:
        if is_perfect_squre(i):
            na.append(nl[count])
            count+=1
        else:
            na.append(i)
    return na



ip = [7, 64, 9, 13, 1, 4, 33, 25, 98]
op = find_perfect_squre(ip)
print(op)
