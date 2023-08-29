import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)

days = []
for i in range(len(trees)):
    days.append(1+(i+1)+trees[i])

print(max(days))