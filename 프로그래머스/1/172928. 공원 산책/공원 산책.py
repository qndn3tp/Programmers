def solution(park, routes):

    # 시작위치 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j         # 시작위치
                break
        else:
            continue
        break

    for r in routes:
        d = r[0]            # 방향
        s = int(r[2])       # 거리

        if d == "E":
            # 공원을 벗어남
            if y + s >= len(park[0]):       
                continue
            # 장애물 체크
            dy = y
            for i in range(s):              
                dy += 1
                if park[x][dy] == "X":
                    break
            else:
                x, y = x, dy

        elif d == "S":
            # 공원을 벗어남
            if x + s >= len(park):       
                continue
            # 장애물 체크
            dx = x
            for i in range(s):              
                dx += 1
                if park[dx][y] == "X":
                    break
            else:
                x, y = dx, y

        elif d == "W":
            # 공원을 벗어남
            if y - s < 0:       
                continue
            # 장애물 체크
            dy = y
            for i in range(s):              
                dy -= 1
                if park[x][dy] == "X":
                    break
            else:
                x, y = x, dy

        elif d == "N":
            # 공원을 벗어남
            if x - s < 0:       
                continue
            # 장애물 체크
            dx = x
            for i in range(s):              
                dx -= 1
                if park[dx][y] == "X":
                    break
            else:
                x, y = dx, y
    return [x, y]