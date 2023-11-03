import sys

n = int(sys.stdin.readline())

list = []
for _ in range(n):
    n, d, m, y = sys.stdin.readline().split()
    d, m, y = map(int, (d, m, y))
    list.append((y, m, d, n))

list.sort()
print(list[-1][3])
print(list[0][3])