import sys

n, m = map(int, sys.stdin.readline().split())

nums = []
for i in range(1, m+1):
    for j in range(i):
        if len(nums) >= m:
            break
        else:
            nums.append(i)

ans = sum(nums[n-1:m])
print(ans)