import sys

n, m = map(int, sys.stdin.readline().split())

a = []          # 도로
b = []          # 연정이가 달린 도로

for _ in range(n):
    road, speed = map(int, sys.stdin.readline().split())
    for i in range(road):
        a.append(speed)

for _ in range(m):
    road, speed = map(int, sys.stdin.readline().split())
    for i in range(road):
        b.append(speed)

over = 0
for i in range(len(b)):
    if b[i] - a[i] > over:
        over = b[i] - a[i]
print(over)