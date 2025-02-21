# Example 1:
#
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
import math


def check_squre(no):
    squared = math.isqrt(no)
    print(squared)

    return no == squared*squared




ip = 81
op = check_squre(ip)
print(op)

