def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha = [i for i in alphabet if i not in skip]

    ans = ""
    for i in s:
        target = alpha[(alpha.index(i) + index) % len(alpha)]
        ans += target
    return ans