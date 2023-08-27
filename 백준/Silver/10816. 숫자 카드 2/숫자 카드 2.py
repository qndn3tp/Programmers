import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 카드 숫자 : 개수 딕셔너리
counter = Counter(cards)

for i in arr:
    if counter.get(i):
        print(counter[i], end=" ")
    else:
        print(0, end=" ")