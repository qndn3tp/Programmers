import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().split()
    ans = ""
    for word in s:
        ans += word[::-1]
        ans += " "
    print(ans)