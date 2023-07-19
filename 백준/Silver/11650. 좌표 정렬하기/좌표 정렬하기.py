import sys

T = int(sys.stdin.readline())

xy = []
for _ in range(T):
    xy.append(list(map(int, sys.stdin.readline().split(" "))))

xy.sort(key = lambda xy: xy[1])
xy.sort(key = lambda xy: xy[0])

for i in xy:
    x = i[0]
    y = i[1]
    print(f"{x} {y}")