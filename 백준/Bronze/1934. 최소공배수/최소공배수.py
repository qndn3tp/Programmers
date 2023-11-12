import sys
from math import lcm

n = int(sys.stdin.readline())
res = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    res.append(lcm(a, b))

for i in res:
    print(i)