from collections import deque

def solution(board, moves):
    res = deque()
    ans = 0
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if len(res) == 0 or res[-1] != board[i][m-1]:
                    res.append(board[i][m-1])
                    board[i][m-1] = 0
                    break
                elif res[-1] == board[i][m-1]:
                    res.pop()
                    board[i][m-1] = 0
                    ans += 2
                    break
            else:
                continue
    return ans