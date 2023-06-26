def solution(name, yearning, photo):
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    print(dict)

    ans = []

    for i in range(len(photo)):
        res = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                res += dict[photo[i][j]]
        ans.append(res)

    return(ans)