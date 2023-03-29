
def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

test = int(input())
for t in range(test):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))