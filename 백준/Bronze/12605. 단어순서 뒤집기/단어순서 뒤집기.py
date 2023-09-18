import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()
    print(f"Case #{i+1}: {' '.join(s[::-1])}")