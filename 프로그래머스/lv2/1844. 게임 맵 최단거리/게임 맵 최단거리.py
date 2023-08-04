from collections import deque

def solution(maps):
    # 동서남북
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()

            # 동서남북 칸 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나는 경우
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                # 벽인 경우
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 동서남북 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    # 재귀

        # 움직인 거리 == 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    
    return -1 if answer == 1 else answer  