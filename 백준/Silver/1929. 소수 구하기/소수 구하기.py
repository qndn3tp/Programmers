import math
import sys

a, b = map(int, sys.stdin.readline().split())

for num in range(a, b+1):
    # 예외) 1은 소수가 아님
    if num == 1:
        continue
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            break
    else:
        print(num)