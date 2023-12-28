from collections import Counter

def solution(spell, dic):
    dic = [i for i in dic if len(i) >= len(spell)]
    ans = 2
    
    for i in dic:
        if ans == 1:
            return ans
        cnt = Counter(i)
        for j in spell:
            if j in cnt and cnt[j] == 1:
                ans = 1
                continue
            else:
                ans = 2
                break
    return ans