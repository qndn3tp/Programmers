import sys

n, k = map(int, sys.stdin.readline().split())

a = set(sys.stdin.readline().split())
b = set(sys.stdin.readline().split())

print(len(a-b) + len(b-a))