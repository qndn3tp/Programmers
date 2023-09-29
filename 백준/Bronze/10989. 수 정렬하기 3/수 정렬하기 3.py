import sys

N = int(sys.stdin.readline())

nums = [0] * 10001
for i in range(N):
    n = int(sys.stdin.readline())
    nums[n] += 1

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)