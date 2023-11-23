def solution(board):
    total = len(board) * len(board[0])

    # 지뢰의 위치 찾기
    bomb = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                bomb.append([i,j])

    # 지뢰가 없거나 모든 지역에 지뢰가 있는 경우
    if len(bomb) == 0 or len(bomb) == total:
        return total - len(bomb)

    # 지뢰 주변 위, 아래, 대각선 탐색
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                board[nx][ny] = 1

    # 가능한 구역 찾기
    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 1:
                ans += 1
    return ans