import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = []

i = 0   # a의 인덱스
j = 0   # b의 인덱스
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

if i < len(a) and j == len(b):
    res += a[i:]
elif i == len(a) and j < len(b):
    res += b[j:]

print(" ".join(map(str, res)))