def solution(l, r):
    res = []
    for i in range(l, r+1):
        j = str(i).replace("5", "")
        j = j.replace("0", "")

        if j == "":
            res.append(i)
    return res if len(res) > 0 else [-1]