import sys
n, l = map(int, sys.stdin.readline().split())
h = sorted(list(map(int, sys.stdin.readline().split())))
for i in h:
    if l >= i:
        l += 1
print(l)