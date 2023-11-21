def solution(numlist, n):
    num = {}
    for i in numlist:
        num[i] = abs(i - n)

    ls = list(num.items())

    ls.sort(key = lambda x: x[0], reverse=True)

    ls.sort(key = lambda x: x[1])

    return [i[0] for i in ls]
    