def solution(common):
    one, two, three = common[:3]

    if two - one == three - two:
        res = common[-1] + (two - one)
    elif two // one == three // two:
        res = common[-1] * (two // one)
    return res