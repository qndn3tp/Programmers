def solution(a, b):
    ls = [i for i in range(min(a,b), max(a,b)+1)]
    return sum(ls)