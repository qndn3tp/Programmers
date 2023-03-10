def solution(new_id):
    # 1단계
    res1 = new_id.lower()
    # 2단계
    res2 = ""
    special = ["-", "_", "."]
    for i in range(len(res1)):
        if res1[i].islower() or res1[i].isdigit() or res1[i] in special:
            res2 += res1[i]
    # 3단계
    res3 = res2[0]
    for i in range(1,len(res2)):
        if res2[i] == "." and res3[-1] == res2[i]:
            pass
        else:
            res3 += res2[i]
    # 4단계
    res4 = res3
    if res4[0] == ".":
        res4 = res4[1:]
    elif res4[-1] == ".":
        res4 = res4[:-1]
    elif res4[0] == "." and res4[-1] == ".":
        res4 = res4[1:-1]
    # 5단계
    res5 = res4
    if len(res5) == 0:
        res5 = "a"
    # 6단계
    res6 = res5
    if len(res5) > 15:
        res6 = res5[:15]
    if res6[-1] == ".":
        res6 = res6[:-1]
    # 7단계
    res7 = res6
    if len(res7) < 3:
        res7 += res7[-1] * (3-len(res7))
    return res7
