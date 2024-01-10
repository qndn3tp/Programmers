def solution(n):
    res = 0
    while n > 0:
        a = n % 10
        n = n // 10
        res += a
    return res