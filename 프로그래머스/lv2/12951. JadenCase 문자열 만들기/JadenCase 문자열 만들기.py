def solution(s):
    ls = s.split(" ")
    res = []
    for i in range(len(ls)):
        if len(ls[i]) == 0:
            res.append("")
            continue
        if ls[i][0].islower():
            word = ""
            word += ls[i][0].upper()
            word += ls[i][1:].lower()
            res.append(word)
        else:
            word = ""
            word += ls[i][0]
            word += ls[i][1:].lower()
            res.append(word)
    return(" ".join(res))