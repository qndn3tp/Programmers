import sys

# 입력
n, m = map(int, sys.stdin.readline().split())

# 듣도 못한 사람
hear = set([])
for _ in range(n):
    hear.add(sys.stdin.readline().strip())
# 보도 못한 사람
see = set([])
for _ in range(m):
    see.add(sys.stdin.readline().strip())

# 듣지도, 보지도 못한 사람(교집합)
res = hear & see
res = sorted(list(res))

# 출력
print(len(res))
for i in res:
    print(i)