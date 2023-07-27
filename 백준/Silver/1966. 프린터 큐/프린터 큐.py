import sys

# 테스트 케이스 개수
T = int(sys.stdin.readline())

ans = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    # 순서, 중요도 쌍
    queue = list(enumerate(queue))

    run = 0
    while True:
        q = queue.pop(0)
        if any(q[1] < i[1] for i in queue):
            queue.append(q)
        else:
            if q[0] == M:
                run += 1
                break
            else:
                run += 1
    ans.append(run)

for i in ans:
    print(i)
