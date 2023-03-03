import itertools
def solution(babbling):
    bb = {"aya": "1", "ye": "2", "woo": "3", "ma": "4"}
    ans = 0

    res = []
    for b in babbling:
        b = b.replace("aya",bb["aya"])
        b = b.replace("ye",bb["ye"])
        b = b.replace("woo",bb["woo"])
        b = b.replace("ma",bb["ma"])
        res.append(b)
    for i in res:
        if i.isdigit():
            isValid = True
            for j in range(len(i)-1):
                if i[j] == i[j+1]:
                    isValid = False
                    break
            if isValid == True:
                ans += 1
    return(ans)