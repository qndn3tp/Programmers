def solution(ans):
    # 문제 찍는 방식
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    # 각 점수
    s1 = 0
    s2 = 0
    s3 = 0
    # 사람과 점수를 dict으로 관리
    score = {1: s1, 2: s2, 3: s3}
    for i in range(len(ans)):
        if ans[i] == p1[i%len(p1)]:
            score[1] += 1
        if ans[i] == p2[i%len(p2)]:
            score[2] += 1
        if ans[i] == p3[i%len(p3)]:
            score[3] += 1
    # 가장 많이 맞춘 사람 뽑기
    res = []
    for k in score:
        if score[k] == max(score.values()):
            res.append(k)
    return(res)