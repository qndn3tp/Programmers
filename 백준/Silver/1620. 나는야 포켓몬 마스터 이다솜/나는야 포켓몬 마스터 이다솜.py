import sys

n, m = map(int, sys.stdin.readline().split())

# 포켓몬 도감 완성
pocketmon1 = {}     # 번호: 이름
pocketmon2 = {}     # 이름: 번호
for i in range(n):
    name = sys.stdin.readline().strip()
    pocketmon1[i+1] = name
    pocketmon2[name] = i+1

# 찾아야할 포켓몬 입력 받기
find = []
for j in range(m):
    s = sys.stdin.readline().strip()
    if s.isalpha():
        find.append(s)
    else:
        find.append(int(s))

# 도감에서 포켓몬 찾기
for f in find:
    try:
        print(pocketmon1[f])
    except:
        print(pocketmon2[f])