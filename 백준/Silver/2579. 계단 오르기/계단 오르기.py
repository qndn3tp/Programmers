import sys

n = int(sys.stdin.readline())
stair = [0]
for _ in range(n):
    stair.append(int(sys.stdin.readline()))
dp = [0] * (n+1)

# 계단이 2개 이하일 때
if len(stair) <= 3:
    print(sum(stair))
# 계단이 3개 이상일 때
else:
    dp[1] = stair[1]               # 첫번째 계단
    dp[2] = stair[1] + stair[2]    # 두번째 계단
    for i in range(3, n+1):        # 세번째 ~ 마지막 계단(점화식)
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])    # 1점프로 오는 경우 / 2점프로 오는 경우
    print(dp[-1])       # 마지막 계단까지 얻은 점수의 최댓값