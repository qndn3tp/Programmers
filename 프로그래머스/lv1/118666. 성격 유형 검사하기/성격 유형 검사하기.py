def solution(survey, choices):
    test = {"R": 0, "T": 0, 
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0 }

    score = {1: 3, 2: 2, 3: 1, 
             4: 0, 
             5: 1, 6: 2, 7: 3}

    for i in list(zip(survey, choices)):
        if i[1] > 4:
            test[i[0][1]] += score[i[1]]
        else:
            test[i[0][0]] += score[i[1]]

    a = "RTCFJMAN" # 알파벳순으로 미리 적어서 점수가 같을 때 해결
    ans = ""
    for i in range(0, 7, 2):
        if test[a[i]] > test[a[i+1]]:
            ans += a[i]
        elif test[a[i]] < test[a[i+1]]:
            ans += a[i+1]
        else:
            ans += a[i]
    return(ans)