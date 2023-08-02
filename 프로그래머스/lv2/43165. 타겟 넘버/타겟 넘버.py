from collections import deque

def solution(numbers, target):
    ans = 0
    queue = deque()
    n = len(numbers)

    # 초기값: numbers의 원소값, 다음 원소를 가리키기 위해 인덱스 사용
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        value, idx = queue.popleft()
        idx += 1
        if idx < n:     # numbers의 원소를 돌며 모두 연산, 결과를 큐에 담음
            queue.append([value + numbers[idx], idx])
            queue.append([value - numbers[idx], idx])
        else:           # 큐에 원소를 다 넣음 (numbers의 원소를 모두 더하거나 뺀 결과)
            if value == target:
                ans += 1
    return ans