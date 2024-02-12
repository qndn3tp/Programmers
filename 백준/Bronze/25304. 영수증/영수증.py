import sys

receipt = int(sys.stdin.readline())
N = int(sys.stdin.readline())

cost = 0
for i in range(N):
    c, n = map(int, sys.stdin.readline().split())
    cost += c * n

if cost == receipt:
    print("Yes")
else:
    print("No")