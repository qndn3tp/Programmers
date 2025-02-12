from collections import Counter
def solution(clothes):
    types = [c[1] for c in clothes]
    counter = Counter(types)
    cnt_list = list(counter.values())
    
    ans = 1
    for cnt in cnt_list:
        ans *= cnt + 1
    return ans - 1