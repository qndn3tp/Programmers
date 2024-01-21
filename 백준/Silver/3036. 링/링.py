def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

import sys
n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
t = ls[0]
ls = ls[1:]
for i in ls:
    g = gcd(t, i)
    print(f"{t//g}/{i//g}")
