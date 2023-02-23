def solution(lottos, win_nums):
    n_inter = len(list(set(lottos) & set(win_nums)))
    n_zeros = lottos.count(0)
    # 0만 있는 경우
    if n_zeros == 6:
        ans = [1, 6]
    else:
        h, l = n_inter + n_zeros, n_inter
        if h <= 1 and l <=1 :
            ans = [6, 6]
        else:
            ans = [7-(n_inter + n_zeros), 7-n_inter]
    return ans