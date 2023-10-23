import sys

# 입력
n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

# 풀이
average = (sum(scores) / max(scores) * 100) / n

# 출력
print(average)