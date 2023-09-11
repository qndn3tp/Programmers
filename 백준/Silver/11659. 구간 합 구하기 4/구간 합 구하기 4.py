import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# (처음 ~ n번)까지의 누적 합을 저장해둠.
res = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        res[i] = nums[0]
    else:
        res[i] = res[i-1] + nums[i]

for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(res[j-1])
    else:
        print(res[j-1] - res[i-2])