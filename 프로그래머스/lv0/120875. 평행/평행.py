def solution(dots):
    # (0,1) (2,3)
    slope01 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    slope23 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    if slope01 == slope23: 
        return 1
    # (0,2) (1,3)
    slope02 = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
    slope13 = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])
    if slope02 == slope13:
        return 1
    # (0,3) (1,2)
    slope03 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    slope12 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    if slope03 == slope12:
        return 1
    return 0