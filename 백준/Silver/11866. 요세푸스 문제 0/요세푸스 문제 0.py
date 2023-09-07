import sys

n, k = map(int, sys.stdin.readline().split())

res = []
nums = [i for i in range(1, n+1)]

i = -1
while len(res) < n:             # 모든 사람이 제거될 때까지
    cnt = 0                     # 3번째 사람을 카운트
    while cnt < k:
        if i == len(nums)-1:    # 마지막과 처음을 이음 (원형 구현)
            i = -1
        if nums[i+1] != 0:      # 제거된 사람이 아니라면 
            i += 1
            cnt += 1            # 3번째가 될 때까지 카운트+1
        else:                   # 이미 제거된 사람은 패스
            i += 1
            continue
    res.append(str(nums[i]))    # 결과에 제거된 사람을 넣음
    nums[i] = 0                 # 제거된 사람은 0으로 구별

print("<" + ", ".join(res) + ">")