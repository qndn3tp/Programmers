def minIndex(list, x):         # keymap들중 더 작은 인덱스를 찾는 함수
    idx = 100
    for ls in list:
        try:
            i = ls.index(x)
            if i == 0:         # 첫번째 인덱스면 최소이기 때문에 바로 리턴
                return 0
            else:
                if i <= idx:   # 더 작은 인데스로 업데이트
                    idx = i
        except:                # 특정 키맵에 해당 알파벳이 없는 경우
            continue
    return idx

def solution(keymap, targets):
    ans = []
    for target in targets:
        cnt = 0
        for t in target:
            idx = minIndex(keymap, t)
            if idx == 100:      # 어느자판에도 존재하지 않는 경우
                ans.append(-1)
                break
            else:
                cnt += idx + 1
        else:
            ans.append(cnt)
    return ans
