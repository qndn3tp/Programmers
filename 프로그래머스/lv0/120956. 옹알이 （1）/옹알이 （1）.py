def solution(babbling):
    speaks = ["aya", "ye", "woo", "ma"]

    cnt = 0
    for b in babbling:
        for s in speaks:
            if b != "":
                b = b.replace(s, " ")
            else:
                break
        if b.strip() == "":
            cnt += 1
    return cnt