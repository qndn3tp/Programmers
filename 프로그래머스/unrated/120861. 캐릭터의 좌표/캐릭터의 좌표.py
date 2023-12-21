def solution(keyinput, board):
    max_x = board[0] // 2       # left, right
    max_y = board[1] // 2       # up, down

    x, y = 0, 0
    for key in keyinput:
        if key == "left":
            if x > -1 * max_x:
                x -= 1
        elif key == "right":
            if x < max_x:
                x += 1
        elif key == "down":
            if y > -1 * max_y:
                y -= 1
        else:
            if y < max_y:
                y += 1

    return [x, y]