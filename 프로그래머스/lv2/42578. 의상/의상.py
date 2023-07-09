import collections
def solution(clothes):

    clothe = collections.Counter(i[1] for i in clothes)

    clothe_cnt = list(clothe.values())

    ans = 1
    for cnt in clothe_cnt:
        ans *= cnt + 1  # 안입는 경우도 포함
    ans -= 1    # 다 안입는 경우

    return ans