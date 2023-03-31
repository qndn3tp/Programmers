import math
def solution(n):
    ans = 0
    for i in range(n//2+1):
        res = [2]*i
        while sum(res) != n:
            res.append(1)
        ans += math.factorial(len(res))//(math.factorial(res.count(1))*math.factorial(res.count(2)))
    return ans%1234567