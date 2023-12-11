def solution(score):
    avg_score = []

    for i in range(len(score)):
        avg_score.append((score[i][0] + score[i][1]) / 2)

    ls = sorted(avg_score, reverse=True)

    res = []
    for i in avg_score:
        res.append(ls.index(i) + 1)
    return res