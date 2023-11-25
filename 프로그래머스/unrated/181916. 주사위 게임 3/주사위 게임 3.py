from collections import Counter

def solution(a, b, c, d):
    ls = [a, b, c, d]
    counter1 = Counter(ls)
    counter2 = {v:k for k, v in counter1.items()}

    # 4
    if len(counter1) == 1:
        return 1111 * a
    # 1, 1, 1, 1
    elif len(counter1) == 4:
        return min(a, b, c, d)
    # 2, 2
    elif len(counter1) == 2 and len(counter2) == 1:
        p, q = min(a,b,c,d), max(a,b,c,d)
        return (p + q) * abs(p - q)
    # 3, 1
    elif len(counter1) == 2 and len(counter2) == 2:
        p, q = counter2[3], counter2[1]
        return (10 * p + q)**2
    # 2, 1, 1
    elif len(counter1) == 3:
        nums = [k for k,v in counter1.items() if v == 1]
        return nums[0] * nums[1]