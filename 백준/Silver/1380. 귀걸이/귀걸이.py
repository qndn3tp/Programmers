import sys

res = []
while True:
    n = int(sys.stdin.readline())
    # 0을 입력하면 종료
    if n == 0:
        break

    # 귀걸이를 압수당한 학생
    name = [sys.stdin.readline().strip() for _ in range(n)]

    # 귀걸이를 잃어버린 사람 번호
    lost = n*(n+1)
    for _ in range(2*n-1):
        s = sys.stdin.readline().split()
        lost -= int(s[0])

    res.append(name[lost-1])

for idx, value in enumerate(res):
    print(idx+1, value)