def solution(n, word):
    res = []
    
    for i in range(len(word)):
        if len(word[i]) == 1:
            return [i%n+1, i//n+1]
        if word[i] in res:
            return  [i%n+1, i//n+1]
        if i < len(word)-1:
            if word[i][-1] != word[i+1][0]:
                return [(i+1)%n+1, (i+1)//n+1]
        res.append(word[i])
    return [0, 0]
