def solution(n, lost, reserve):

    # 여벌 체육복을 도난 당한 사람
    inter = list(set(lost) & set(reserve))
    # 여벌 체육복을 도난 당한 경우, 다른 사람에게 빌려주지 않고 본인이 입는 걸로 제한 -> 중복 제거
    lost = list(set(lost) - set(inter))
    reserve = list(set(reserve) - set(inter))

    lost.sort()
    reserve.sort()

    # 먼저, 결과값은 체육복을 하나만 가진사람으로 고정
    ans = n - len(lost)

    # 만약 체육복을 줄 수 있는 범위라면 앞 번호를 주는 게 무조건 나음.(뒤는 겹칠 수도)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if abs(reserve[i] - lost[j]) == 1:
                ans += 1
                lost = lost[1:]
                break

    return(ans)