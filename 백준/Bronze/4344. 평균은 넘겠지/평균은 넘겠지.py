import sys

t = int(sys.stdin.readline())

for _ in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    n = score[0]            # 학생의 수
    score = score[1:]       # 학생 N명의 점수
    avg = sum(score) / n    # 평균

    cnt = 0                 # 점수가 평균을 넘는 학생의 수
    for sc in score:
        if sc > avg:
            cnt += 1

    res = cnt / n * 100
    print('%.3f' %res + "%")