import sys

a, b ,v = map(int, sys.stdin.readline().split())

k = (v-b) / (a-b)

if k == int(k):
    print(int(k))
else:
    print(int(k) + 1)