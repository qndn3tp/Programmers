def solution(quiz):
    ans = []

    for i in quiz:
        idx = i.index("=")
        calc = i[:idx-1]
        res = int(i[idx+2:])

        if eval(calc) == res:
            ans.append("O")
        else:
            ans.append("X")
    return ans