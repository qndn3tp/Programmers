x = int(input())

cnt = 0
n = 64  # 초기 막대 크기

while x > 0:
    if n > x:
        n //= 2
    else:
        cnt += 1
        x -= n
print(cnt)