# 회의실 문제
# 가장 많이 미팅을 잡으려면 빨리 끝나는 순서대로 
# 단 정렬은 2개 (빨리 끝나는순, 빨리 시작하는 순)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

ls.sort(key = lambda x: (x[1], x[0]))

res = []
for i in ls:
    if len(res) == 0:
        res.append(i)
    else:
        if res[-1][1] <= i[0]:
            res.append(i)
print(len(res))