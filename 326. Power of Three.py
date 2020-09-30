import math
def isPowerOfThree( n):
    return n > 0 and 3 ** round(math.log(n,3)) == n


print(isPowerOfThree(243))