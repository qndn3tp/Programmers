import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque([str(i) for i in range(1, n+1)])

res = []
while len(cards) > 1:
    res.append(cards.popleft())
    cards.append(cards.popleft())
res.append(cards[0])

print(" ".join(res))