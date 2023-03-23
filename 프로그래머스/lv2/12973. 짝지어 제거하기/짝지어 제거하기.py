def solution(s):
    res = []
    res.append(s[0])

    for i in range(1, len(s)):
        if len(res) > 0:
            if s[i] != res[-1]:
                res.append(s[i])
            else:
                res.pop()
        else:
            res.append(s[i])

    if len(res) == 0:
        return(1)
    else:
        return(0)