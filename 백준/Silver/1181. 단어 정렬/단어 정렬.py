import sys

t = int(sys.stdin.readline())
ls = [sys.stdin.readline().strip() for _ in range(t)]

ls = list(set(ls)) # 중복 제거

ls.sort()          # 정렬 -> 사전순
ls = sorted(ls, key = lambda x: len(x)) # 정렬 -> 길이순
for s in ls:
    print(s)