import sys

# 입력
n, k = map(int, sys.stdin.readline().split())
medal = []
for _ in range(n):
    medal.append(list(map(int, sys.stdin.readline().split())))

# 금,은,동 개수 순서로 정렬
medal.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

# k 국가가 몇 등인지 찾기
for i in range(n):
    if medal[i][0] == k:
        idx = i
        break

# 공동 등수가 있는지 확인
for i in range(n):
    if medal[idx][1:] == medal[i][1:]:
        print(i + 1)
        break