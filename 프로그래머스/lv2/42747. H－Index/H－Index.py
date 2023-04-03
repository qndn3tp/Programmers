def solution(c):
    if max(c) == 0:     # 모두 0인경우
        return 0
    res = []
    for i in range(max(c)+1):
        h = 0   # _번 이상 인용된 논문의 수
        l = 0   # 나머지 논문의 수
        for j in c:
            if i <= j:
                h += 1
            else:
                l += 1
        if h >= i and l <= i:
            res.append(i)
    if len(res) == 0:
        return 0
    else:
        return(res[-1])