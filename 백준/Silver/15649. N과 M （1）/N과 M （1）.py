import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

data = [i for i in range(1, N+1)]

per = permutations(data, M)

for i in per:
    ans = ""
    for j in i:
        ans += str(j)
        ans += " "
    ans.strip()
    print(ans)