import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

m = max(score)

ans = 0
for sc in score:
    ans += sc / m * 100

print(ans/len(score))