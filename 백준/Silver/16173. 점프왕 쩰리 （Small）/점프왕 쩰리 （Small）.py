import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

direction = [(1, 0), (0, 1)]

def jump(x, y, visited):
    if x >= n or x <= -1 or y >= n or y <= -1:
        return False
    if visited[x][y]:
        return False
    if board[x][y] == 0:
        return False
    if board[x][y] == -1:
        print("HaruHaru")
        exit()
    visited[x][y] = True
    for dx, dy in direction:
        next_x = x + dx * board[x][y]
        next_y = y + dy * board[x][y]
        jump(next_x, next_y, visited)
    return True

if jump(0, 0, visited) == True:
    print('Hing')