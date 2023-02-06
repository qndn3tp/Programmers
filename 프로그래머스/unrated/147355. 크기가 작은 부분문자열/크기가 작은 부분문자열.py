def solution(t, p):
    strings = []
    cnt = 0

    l = len(p)

    for i in range(len(t)-l+1):
        strings.append(t[i:i+l])

    for s in strings:
        if int(s) <= int(p):
            cnt += 1
    
    return cnt