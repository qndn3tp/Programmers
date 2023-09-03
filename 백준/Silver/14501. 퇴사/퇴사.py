import sys

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

# 상담 수익의 누적합
cost = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if cost[j] < cost[i] + schedule[i][1]:
            cost[j] = cost[i] + schedule[i][1]

print(cost[-1])