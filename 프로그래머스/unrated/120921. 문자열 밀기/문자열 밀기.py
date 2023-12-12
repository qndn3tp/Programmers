from collections import deque

def solution(A, B):
    dq = deque(list(A))

    if A == B:
        return 0
    
    cnt = 0
    for i in range(len(A)-1):
        dq.appendleft(dq.pop())
        cnt += 1

        if dq == deque(list(B)):
            return cnt
        
    return -1
