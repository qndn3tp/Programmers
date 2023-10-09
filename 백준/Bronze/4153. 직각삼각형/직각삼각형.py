import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if sum(nums) == 0:
        break

    c = max(nums)

    res = [n**2 for n in nums if n != c]

    if sum(res) == c**2:
        print("right")
    else:
        print("wrong")