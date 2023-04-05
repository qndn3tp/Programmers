from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine) # 귤의 크기-귤의 개수
    res = 0    
    n = 0       
    for v in sorted(counter.values(), reverse=True):
        if n < k:
            n += v
            res += 1
    return(res)