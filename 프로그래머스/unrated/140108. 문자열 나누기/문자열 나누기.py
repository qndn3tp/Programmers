def solution(s):
    t = ["", 0, 0] # 첫번째 문자, 같은 문자 카운트, 다른 문자 카운트
    ans = 0
    for i in s:
        # 첫번째 문자 x 지정
        if t[0] == "":
            t[0] = i
            t[1] += 1
        else:
            if t[0] == i:
                t[1] += 1
            else:
                t[2] += 1
            if t[1] == t[2]:
                ans += 1
                t = ["", 0, 0]
    # 두 횟수가 다른 상태에서 더 읽을 글자가 없는 경우
    if t != ["", 0, 0]:
        ans += 1
    return ans
