import sys

N = int(sys.stdin.readline())

xy = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xy.append([x, y])

xy.sort(key = lambda xy: xy[0])
xy.sort(key = lambda xy:xy[1])

for i in xy:
    x, y = i[0], i[1]
    print(x, y)