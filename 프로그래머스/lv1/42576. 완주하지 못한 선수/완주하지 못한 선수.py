def solution(participant, completion):
    dict = {}
    # 참여자
    for p in participant:
        if p not in dict:
            dict[p] = 1
        else:
            dict[p] += 1
    # 참여자-완주자
    for cp in completion:
        if cp in dict:
            dict[cp] -= 1
    for k in dict:
        if dict[k] == 1:
            return(k)