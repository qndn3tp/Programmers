import sys
input = sys.stdin.readline

def knapsack():
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            else:
                # 최대 허용 무게를 넘어 못채우는 경우
                if i < ls[j-1][0]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = max(dp[i - ls[j-1][0]][j-1] + ls[j-1][1], dp[i][j-1])
    print(dp[k][n])

if __name__ == "__main__":
    n, k = map(int, input().split())
    ls = []
    for _ in range(n):
        ls.append(list(map(int, input().split())))
    knapsack()