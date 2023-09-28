import sys

n = int(sys.stdin.readline())

ans = list(sys.stdin.readline().strip())

for _ in range(n-1):
    s = list(sys.stdin.readline().strip())
    for i in range(len(s)):
        if ans[i] != s[i]:
            ans[i] = "?"

print("".join(ans))