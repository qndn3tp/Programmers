def solution(dart):
    # 옵션 규칙
    op = {"*": 2, "#": -1}
    # 보너스 규칙
    bonus = {"S": 1, "D": 2, "T": 3}

    # 문자열 세트 1
    if dart[2] not in op and dart[2] not in bonus:
        ss1 = dart[:2]
        dart = dart[2:]
    else:
        ss1 = dart[:3]
        dart = dart[3:]
    # 문자열 세트 2
    if dart[2] not in op and dart[2] not in bonus:
        ss2 = dart[:2]
        dart = dart[2:]
    else:
        ss2 = dart[:3]
        dart = dart[3:]
    # 문자열 세트 3
    ss3 = dart

    ss = [ss1,ss2,ss3]

    # 로직
    ans_ls = []
    for s in ss:
        if len(s) == 2:
            ans_ls.append(int(s[0]) ** bonus[s[1]])
        else:
            if s[2] == "*":
                # 첫번째에 "*"가 나올 경우 예외처리
                if ss.index(s) != 0:
                    ans_ls[ss.index(s)-1] *= op["*"]
                ans_ls.append(int(s[0]) ** bonus[s[1]] * op["*"])
            elif s[2] == "#":
                ans_ls.append(int(s[0]) ** bonus[s[1]] * op["#"])
            # 점수가 두 자리인 경우
            else:
                ans_ls.append(int(s[:2]) ** bonus[s[2]])

    return(sum(ans_ls))