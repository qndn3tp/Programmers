import math

def find_pn(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    ans = 0
    for num in range(1, n+1):
        if find_pn(num) == True:
            ans += 1
        else:
            continue
    return ans