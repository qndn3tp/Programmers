import sys

e, s, m = map(int, sys.stdin.readline().split())
ne, ns, nm = 1, 1, 1

year = 1
while True:
    if ne == e and ns == s and nm == m:
        break
    ne += 1
    ns += 1
    nm += 1
    year += 1
    if ne > 15:
        ne = 1
    if ns > 28:
        ns = 1
    if nm >  19:
        nm = 1
print(year)