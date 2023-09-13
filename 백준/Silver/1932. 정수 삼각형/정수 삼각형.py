import sys

n = int(sys.stdin.readline())
d = []
for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:                  # only 대각선 왼쪽
            d[i][j] += d[i-1][j]
        elif j == len(d[i]) - 1:    # 대각선 왼쪽과 오른쪽 중 큰 것 선택
            d[i][j] += d[i-1][j-1]
        else:                       # only 대각선 오른쪽
            d[i][j] = d[i][j] + max(d[i-1][j-1], d[i-1][j])

print(max(d[-1]))