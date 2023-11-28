from collections import Counter

def solution(array):
    counter = Counter(array)
    ls = list(counter.items())
    
    if len(ls) == 1:
        return ls[0][0]
    ls.sort(key = lambda x: x[1], reverse = True)
    
    return -1 if ls[0][1] == ls[1][1] else ls[0][0]
