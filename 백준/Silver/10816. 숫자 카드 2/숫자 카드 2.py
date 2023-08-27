import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 카드 숫자 : 개수 딕셔너리
cards_cnt = {}
for c in cards:
    if c in cards_cnt:
        cards_cnt[c] += 1
    else:
        cards_cnt[c] = 1

for i in arr:
    if cards_cnt.get(i):
        print(cards_cnt[i], end=" ")
    else:
        print(0, end=" ")