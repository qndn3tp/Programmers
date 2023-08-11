import sys

N, M = map(int, sys.stdin.readline().split())
mat_a = []
for _ in range(N):
    mat_a.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
mat_b = []
for _ in range(M):
    mat_b.append(list(map(int, sys.stdin.readline().split())))

mat = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            mat[n][k] += mat_a[n][m] * mat_b[m][k]

for n in range(N):
    print(" ".join(map(str, mat[n])))