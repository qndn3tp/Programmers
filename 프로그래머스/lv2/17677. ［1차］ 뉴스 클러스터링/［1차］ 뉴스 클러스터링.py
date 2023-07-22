def solution(str1, str2):
    # 1. 입력 문자열로 다중집합의 생성
    ls1 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            ls1.append((str1[i] + str1[i+1]).lower())

    ls2 = []
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            ls2.append((str2[i] + str2[i+1]).lower())

    # 2. 교집합, 합집합
    inter, union = 0, 0
    check = []  # 이미 처리한 중복
    for i in ls1:
        if i in ls2:
            if i not in check:
                inter += min(ls1.count(i), ls2.count(i))
                union += max(ls1.count(i), ls2.count(i))
                check.append(i)
            else:
                continue
        else:
            union += 1
    for i in ls2:   # 합집합 추가 작업
        if i not in check:
            union += 1

    ans = 1 if inter == 0 and union == 0 else inter/union

    return int(ans * 65536)