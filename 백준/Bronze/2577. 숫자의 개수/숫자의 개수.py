import sys
from functools import reduce
data = [int(sys.stdin.readline()) for _ in range(3)]

res = reduce(lambda x, y : x * y, data)

nums = [i for i in str(res)]

for n in range(10):
    print(nums.count(str(n)))