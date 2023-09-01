import sys

n, k = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
print(sorted(nums)[k-1])