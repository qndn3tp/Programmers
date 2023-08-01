import sys
from collections import deque

# DFS 알고리즘 
def dfs(matrix, i, visited):
    visited[i] = True
    print(i, end=" ")
    for c in range(len(matrix[i])):    # i 노드와 연결된 노드 체크, 재귀적으로 확인
        if matrix[i][c] == 1 and not visited[c]:
            dfs(matrix, c, visited)

# BFS 알고리즘
def bfs(matrix, i, visited):
    queue = deque()    # 큐 생성
    queue.append(i)    # 노드를 꺼내서 큐에 삽입
    while queue:
        value = queue.popleft()    # 가장 먼저 들어온 노드를 꺼냄
        if not visited[value]:
            print(value, end=" ")
            visited[value] = True   
            for c in range(len(matrix[value])):    # i 노드와 연결된 노드 체크, 큐에 추가
                if matrix[value][c] == 1 and not visited[c]:
                    queue.append(c)

# 입력
n, m, v = map(int, sys.stdin.readline().split())

# 연결 리스트, 방문한 노드 리스트 생성
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

# 연결 리스트 완성
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

dfs(matrix, v, visited)
print()
visited = [False] * (n+1)
bfs(matrix, v, visited)