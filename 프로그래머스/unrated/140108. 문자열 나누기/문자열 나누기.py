def solution(s):
    x = s[0]
    x_cnt, y_cnt = 0 , 0

    ans = 0
    for i in range(len(s)):
        if s[i] == x:   # x와 같은 글자 카운트
            x_cnt += 1
        else:           # 다른 글자 카운트
            y_cnt += 1
        if x_cnt != 0 and x_cnt == y_cnt:
            ans += 1
            x_cnt, y_cnt = 0 , 0
            if i < len(s)-1:
                x = s[i+1]    
        # 두 횟수가 다른 상태에서 더 읽은 글자가 없는 경우
        elif x_cnt != y_cnt and i == len(s)-1:
            ans += 1
    return(ans)
