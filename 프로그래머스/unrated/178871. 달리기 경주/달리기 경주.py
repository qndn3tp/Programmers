def solution(players, callings):
    p = {player:rank for rank, player in enumerate(players)} # 선수:등수
    r = {rank:player for rank, player in enumerate(players)} # 등수:선수
    for c in callings:
        i = p[c]    # 현재 등수
        i_front = i-1   # 앞 등수
        front  = r[i_front] # 앞 선수

        r[i] = front
        r[i_front] = c

        p[c] = i_front
        p[front] = i

    return(list(r.values()))