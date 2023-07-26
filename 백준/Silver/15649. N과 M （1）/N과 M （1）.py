import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

data = [i for i in range(1, N+1)]

for i in permutations(data, M):
    ans = ""
    for j in i:
        ans += str(j)
        ans += " "
    ans.strip()
    print(ans)