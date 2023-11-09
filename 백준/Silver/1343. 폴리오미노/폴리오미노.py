import sys

s = sys.stdin.readline().strip()

s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")

for i in s:
    if i == "X":
        print(-1)
        break
else:
    print(s)