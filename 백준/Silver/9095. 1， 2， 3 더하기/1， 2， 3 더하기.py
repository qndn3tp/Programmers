import sys

T = int(sys.stdin.readline())
tc = [int(sys.stdin.readline().strip()) for _ in range(T)]

for n in tc:
    # 1,2,3은 규칙에서 제외됨. 따로 추가해줘야함.
    if n == 1:
       print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    
    else:
        dp = [0] * (n+1)    # 0부터 n까지 저장해야되기 때문.
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[-1])