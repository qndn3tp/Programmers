def solution(sizes):
    for s in sizes:
        s[0], s[1] = max(s[0], s[1]), min(s[0], s[1])
    return max([sizes[i][0] for i in range(len(sizes))]) * max([sizes[i][1] for i in range(len(sizes))])
