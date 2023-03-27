def solution(n):
    cnt = 0
    while n > 0: 
        if n % 2 == 0: # 두 배로 이동가 능(순간이동)
            n -= n//2 # 남은 칸
        else:   # 두 배로 이동 불가(점프)
            n -= n%2    # 남은 칸
            cnt += 1 # 점프 시 배터리 사용+1
    return(cnt)