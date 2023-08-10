import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

out = []
res = []

def dfs():
    if len(out) == m and sorted(out) not in res:
        res.append(sorted(out))
        print(" ".join(map(str, out)))
        return
    
    for i in nums:
        if i not in out:
            out.append(i)
            dfs()
            out.pop()
dfs()