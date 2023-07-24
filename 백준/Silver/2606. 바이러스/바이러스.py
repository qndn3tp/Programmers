import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
cnt = -1

def DFS(v):
    visited[v] = True
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
DFS(1)
print(cnt)