def solution(wallpaper):
    start = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                start.append([i, j])

    start_x = min([i[0] for i in start])
    start_y = min(i[1] for i in start)

    end_x = max(i[0] for i in start) + 1
    end_y = max(i[1] for i in start) + 1

    return  [start_x, start_y, end_x, end_y]