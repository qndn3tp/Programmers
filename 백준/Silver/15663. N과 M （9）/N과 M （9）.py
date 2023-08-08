import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

perm = sorted(list(set(list(permutations(nums, m)))))

for i in perm:
    res = " ".join(str(j) for j in i)
    print(res)