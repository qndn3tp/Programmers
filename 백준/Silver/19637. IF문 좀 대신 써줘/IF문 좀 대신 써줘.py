import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

title = []
value = []
for _ in range(n):
    a, b = input().rstrip().split()
    title.append(a)
    value.append(int(b))

character = [int(input().rstrip()) for i in range(m)]

for i in range(m):
    idx = bisect_left(value, character[i])
    print(title[idx])