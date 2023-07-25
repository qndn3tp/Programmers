import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().strip().split())

data = [i for i in range(1, n+1)]

ans = list(combinations(data, m))
for i in ans:
    s = ""
    for j in i:
        s += str(j)
        s += " "
    s.strip()
    print(s)