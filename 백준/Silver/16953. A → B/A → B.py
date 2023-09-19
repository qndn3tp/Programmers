import sys

a, b = map(int, sys.stdin.readline().split())

cnt = 1
while b != a:
    cnt += 1
    temp = b
    if b % 2 == 0:      # 2로 나눠지는 경우
        b //= 2
    elif b % 10 == 1:   # 끝자리 수가 1인 경우
        b //= 10
    if temp == b:       # 두 연산을 했지만 값이 바뀌지 않는 경우(두 연산 모두에 포함되지 않는 경우) 
        print(-1)
        break
else:
    print(cnt)