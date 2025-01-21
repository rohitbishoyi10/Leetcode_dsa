# Given a positive integer n, write a function that returns the number of
# set bits
#  in its binary representation (also known as the Hamming weight).


def hamming_weight(n):
    count = 0
    while n > 0:
        count += n & 1  # Check if the last bit is 1
        n >>= 1  # Right shift n by 1 to process the next bit
    return count

# Example usage
print(hamming_weight(11))  # Output: 3 (11 in binary is 1011)
