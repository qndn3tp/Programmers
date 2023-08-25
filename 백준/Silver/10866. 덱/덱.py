import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()

for _ in range(N):
    data = sys.stdin.readline().split()

    if data[0] == "push_front":
        deq.appendleft(int(data[1]))
    
    elif data[0] == "push_back":
        deq.append(int(data[1]))

    elif data[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

    elif data[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())

    elif data[0] == "size":
        print(len(deq))

    elif data[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif data[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif data[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])