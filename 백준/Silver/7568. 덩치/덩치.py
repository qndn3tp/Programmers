import sys

size = []
t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().strip().split())
    size.append([w,h])

numbering = []
for i in range(len(size)):
    cnt = 0
    for j in range(len(size)):
        if i == j:
            continue
        if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            cnt += 1
    numbering.append(cnt+1)

for num in numbering:
    print(num, end=" ")