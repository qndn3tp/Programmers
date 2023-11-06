import sys

s = sys.stdin.readline().strip()

res = []

for i in range(len(s)):
    res.append(s[i:])

for i in sorted(res):
    print(i)