# 사과상자 하나의 판매 이익
def make_box(box, m):
    return box[-1] * m

def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    answer = 0
    for i in range(len(sorted_score)//m):
        res = make_box(sorted_score[m*i:m*(i+1)], m)
        answer += res
    return answer