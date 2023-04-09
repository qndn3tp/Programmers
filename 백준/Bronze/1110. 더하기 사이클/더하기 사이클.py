import sys

n = int(sys.stdin.readline())

if n < 10:
    n *= 10

num = n
cnt  = 0
while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10 # 합의 가장 오른쪽 자리수
    num = int(str(num%10) + str(c))
    cnt += 1

    if (num == n):
        break
print(cnt)