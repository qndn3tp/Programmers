import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]

for p in product(nums, repeat=m):
    s = " ".join(str(i) for i in p)
    print(s)