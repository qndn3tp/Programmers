import sys

n = int(sys.stdin.readline())

ans = 0
for _ in range(n):
    c, k = map(int, sys.stdin.readline().split())
    if k == 1:
        ans += c
    else:
        ans += c * k
print(ans)