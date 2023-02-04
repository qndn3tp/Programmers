def solution(d, budget):
    cnt = 0

    d.sort()

    cost = 0
    # 정렬 후, 원소를 하나씩 예산이 넘는지 점검 + 카운트
    for c in d:
        cost += c
        if cost <= budget:
            cnt += 1
        else:
            break
            
    return cnt