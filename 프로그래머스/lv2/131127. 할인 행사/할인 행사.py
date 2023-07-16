import collections

def solution(want, number, discount):
    order = {want[i]:number[i] for i in range(len(want))}
    day = 0
    for i in range(len(discount)-10+1):
        ls = discount[i:i+10]
        ls_count = dict(collections.Counter(ls))
        if ls_count == order:
            day += 1
    return day