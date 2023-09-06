import sys

n,m = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))[::-1]     # 뽑아내려고 하는 수의 위치. 큐는 원소를 앞에 못넣기 때문에 역순으로 타겟팅

res = 0     # 2,3번 연산 횟수

queue = [i for i in range(1, n+1)]      

while len(queue) > (n-m) and len(target) > 0:
    t = target.pop()
    idx = queue.index(t)
    # 맨 왼쪽에 위치하면 (1번 연산)
    if idx == 0:
        queue.pop(0)
    # 중간보다 앞쪽에 위치하면 (2번 연산)
    elif idx <= len(queue)//2:
        temp = queue.pop(0)
        queue.append(temp)
        res += 1
        target.append(t)
    # 중간보다 뒷쪽에 위치하면 (3번 연산)
    else:
        temp = [queue.pop()]
        queue = temp + queue
        res += 1
        target.append(t)

print(res)