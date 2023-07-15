def solution(s):
    # 문자열로 표현된 집합 => 리스트
    s = s[2:-2]
    s = s.split("},{") 
    s.sort(key = len)
    ls = []
    for i in s:
        ls.append(i.split(","))

    # 메인 로직
    res = []
    for i in ls:
        for j in i:
            # 초기값
            if len(res) == 0:
                res.append(j)
            else:
                if j not in res:
                    res.append(j)
    return list(map(int, res))