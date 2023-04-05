def solution(k, tangerine):
    # 직접 dic 생성: 귤 크기-귤 개수
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # value를 기준으로 정렬, 파악
    ls = sorted(dic.values(), reverse=True)

    res = 0
    n_tangerine = 0
    for v in ls:
        if n_tangerine < k:
            n_tangerine += v
            res += 1
    return(res)