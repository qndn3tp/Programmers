import sys

i = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if (l + p + v) == 0:
        break
    ans = ((v // p) * l) + min((v % p), l)
    print(f"Case {i}: {ans}")
    i += 1