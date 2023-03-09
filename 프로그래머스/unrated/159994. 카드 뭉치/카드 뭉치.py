from collections import deque
def solution(cards1, cards2, goal):
    card1_q = deque(cards1)
    card2_q = deque(cards2)
    ans = "Yes"
    for word in goal:
        if card1_q and card1_q[0] == word:
            card1_q.popleft()
        elif card2_q and card2_q[0] == word:
            card2_q.popleft()
        else:
            ans = "No"
    return(ans)