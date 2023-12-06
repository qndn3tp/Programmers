def solution(n):

    res = [[0 for _ in range(n)] for __ in range(n)]

    x, y = 0, 0
    dir = "right"

    for num in range(1, n * n + 1):
        res[x][y] = num

        if dir == "right":
            if y == n - 1 or res[x][y + 1] != 0:
                dir = "down"
                x += 1
            else:
                y += 1

        elif dir == "down":
            if x == n - 1 or res[x + 1][y] != 0:
                dir = "left"
                y -= 1
            else:
                x += 1

        elif dir == "left":
            if y == 0 or res[x][y - 1] != 0:
                dir = "up"
                x -= 1
            else:
                y -= 1

        elif dir == "up":
            if x == 0 or res[x - 1][y] != 0:
                dir = "right"
                y += 1
            else:
                x -= 1

        num += 1

    return res