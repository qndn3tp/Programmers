def solution(participant, completion):
    dict = {}
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    for c in completion:
        if c in dict:
            dict[c] -= 1
    
    for item in dict.items():
        if item[1] == 1:
            return item[0]