import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

perm = sorted(list(permutations(nums, m)))

for p in perm:
    s = " ".join(str(i) for i in p)
    print(s)