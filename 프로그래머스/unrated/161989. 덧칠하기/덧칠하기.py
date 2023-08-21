def solution(n, m, section):
    ans = 0

    while len(section) > 0:
        wall = section[0]   # 칠해야 할 벽 중 첫번째
        for i in range(m):  # 롤러의 길이만큼 
            if len(section) > 0:
                if wall == section[0]:   # 현재 칠하고 있는 벽이 벗겨진 벽이라면
                    section.pop(0)     # 벽을 칠하고 리스트에서 제거
            wall += 1   # 그 다음 벽 검사
        ans += 1

    return ans