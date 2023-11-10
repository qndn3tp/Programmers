import sys
from math import gcd

n = int(sys.stdin.readline())

tree = []           # 나무들의 위치
term = []           # 나무들의 간격
for i in range(n):
    t = int(sys.stdin.readline())
    if i == 0:
        tree.append(t)
    else:
        term.append(t-tree[-1])
        tree.append(t)

# 간격 찾기 -> 간격들의 최대공약수
g = term[0]
for j in range(1, len(term)):
    g = gcd(g, term[j])

# 필요한 나무 수
res = 0
for t in term:
    res += t // g - 1
print(res)