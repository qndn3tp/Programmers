def solution(strings, n):
    
    # 1. 사전 순으로 정렬
    strs = sorted(strings)
    # 2. n번째 글자를 기준으로 정렬
    strs = sorted(strs, key = lambda x:x[n])
    
    return strs