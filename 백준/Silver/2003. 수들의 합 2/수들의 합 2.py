import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
l, r = 0, 1
while r <= n and l<=r:
    s = sum(nums[l:r])

    if s == m:
        cnt += 1
        l += 1
        r = l + 1
    
    elif s < m:
        r += 1
    
    else:
        l += 1
        r = l + 1
print(cnt)