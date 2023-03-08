def solution(cards1, cards2, goal):
    c1, c2 = 0, 0
    for i in goal:
        if i in cards1:
            if cards1.index(i) > c1:
                return "No"
            else:
                c1 += 1
        elif i in cards2:
            if cards2.index(i) > c2:
                return "No"
            else:
                c2 += 1
    return "Yes"