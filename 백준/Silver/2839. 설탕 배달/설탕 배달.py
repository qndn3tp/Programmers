import sys
n = int(sys.stdin.readline())

def solution(n):
    basket = 0

    while n > 0:
        # 5의 배수면 그냥 5로 나누면 됨
        if n % 5 == 0:
            basket += n // 5
            n = 0
            break
        n -= 3
        basket += 1

    if n != 0:
        basket = -1

    return basket

print(solution(n))