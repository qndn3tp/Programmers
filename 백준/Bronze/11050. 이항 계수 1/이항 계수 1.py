import sys

n, k = map(int, sys.stdin.readline().split())

res = 1

for i in range(k):
    res *= n
    n -= 1

divisor = 1
for i in range(2, k+1):
    divisor *= i

print(res//divisor)