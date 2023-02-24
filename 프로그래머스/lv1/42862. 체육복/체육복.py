def solution(n, lost, reserve):
    inter = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(inter))
    reserve = list(set(reserve) - set(inter))
    lost.sort()
    reserve.sort()
    ans = n - len(lost)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if abs(reserve[i] - lost[j]) <= 1:
                ans += 1
                lost = lost[1:]
                break
    return ans