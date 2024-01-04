def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        s = ""
        for ch in tree:
            if ch in skill:
                s += ch

        if skill[:len(s)] == s:
            cnt += 1
    return cnt