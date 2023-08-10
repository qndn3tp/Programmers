import sys

n, m = map(int, sys.stdin.readline().split())

out = []

def dfs(start):
    if len(out) == m:
        print(" ".join(map(str, out)))
        return
    
    for i in range(start, n+1):
        out.append(i)
        dfs(i)
        out.pop()
dfs(1)