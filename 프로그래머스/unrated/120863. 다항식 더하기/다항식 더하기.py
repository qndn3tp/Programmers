def solution(polynomial):
    p = polynomial.replace(" + ", " ").split(" ")

    ax = 0
    b = 0

    for i in p:
        if i[-1] == "x":
            if i == "x":
                ax += 1
            else:
                ax += int(i[:-1])
        else:
            b += int(i)

    ax = str(ax) if ax != 1 else ""

    if ax == "0":     # 상수항 뿐인 경우
        return str(b)
    elif b == 0:    # 일차항 뿐인 경우
        return ax + "x"
    return ax + "x" + " + " + str(b)
        