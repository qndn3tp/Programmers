import sys

# 과목평점
grade = {"A+": 4.5, "A0": 4.0,
         "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0,
         "D+": 1.5, "D0": 1.0,
         "F": 0}

data = []
for _ in range(20):
    s = sys.stdin.readline().split()
    data.append(s[1:])

# 전공과목별 합
res = 0
# 학점의 총합
total= 0

for d in data:
    if d[1] != "P":
        res += float(d[0]) * grade[d[1]]
        total += float(d[0])

print('%.6f' %(res / total))