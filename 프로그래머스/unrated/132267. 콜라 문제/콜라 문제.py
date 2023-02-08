def solution(a, b, n):
    ans = 0
    while n // a > 0:
        bottle = (n // a) * b
        ans += bottle
        n = bottle + (n % a)
    return ans