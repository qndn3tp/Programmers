def solution(rank, attendance):
    ls = sorted(list(enumerate(rank)), key = lambda x: x[1])

    res = []
    for i in range(len(ls)):
        if len(res) < 3 and attendance[ls[i][0]] == True:
            res.append(ls[i][0])
    return 10000 * res[0] + 100 * res[1] + res[2]