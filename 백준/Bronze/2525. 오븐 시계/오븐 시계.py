import sys

h, m = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

hh = (m + n) // 60
mm = (m + n) % 60

h += hh
m = mm

if h >= 24:
    h = h % 24
print(h, m)