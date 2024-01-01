import sys
s = sys.stdin.readline().strip()

ans = ""
for i in s:
    if i.islower():
        ans += i.upper()
    else:
        ans += i.lower()

print(ans)