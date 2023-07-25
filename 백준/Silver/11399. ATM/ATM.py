import sys

T = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().strip().split(" ")))
time.sort()

ans = 0
for i in range(len(time)):
    ans += time[i] * (T-i)
print(ans)