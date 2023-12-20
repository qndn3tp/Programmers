import math
def solution(a, b):
    b //= math.gcd(a, b)
    while b > 1:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            return 2
    return 1
