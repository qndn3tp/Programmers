from itertools import permutations

def solution(k, dungeons):
    data = [i for i in range(len(dungeons))]
    order = permutations(data, len(dungeons))

    cnt_list = []   # 각 경우에 따른 던전 수
    for i in order:
        hp = k      # 피로도
        cnt = 0     # 탐험한 던전 수 
        for j in i:
            # 현재 체력 >= 최소 피로도
            if hp >= dungeons[j][0]:
                hp -= dungeons[j][1]
                cnt += 1
            else:
                break
        if cnt == len(dungeons):    # 탐험한 던전 수 가 최대인 경우
            return cnt
        else:
            cnt_list.append(cnt)

    return max(cnt_list)