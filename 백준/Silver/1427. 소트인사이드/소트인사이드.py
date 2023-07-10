import sys

n = int(sys.stdin.readline())
ls = [i for i in str(n)]
ls.sort(reverse=True)
ans = int("".join(ls))
print(ans)