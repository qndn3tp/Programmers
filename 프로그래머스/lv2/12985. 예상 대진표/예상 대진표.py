def solution(n,a,b):
    ls = [i for i in range(1,n+1)]
    ls[a-1] = "a"
    ls[b-1] = "b"
    round = 0
    
    # N명이 있을 때, 총 라운드 수 구하기
    sqrt = 0
    while n > 1:
        n //= 2
        sqrt += 1

    for j in range(sqrt):
        win = []
        for i in range(0, len(ls), 2):
            if ls[i] == "a" and ls[i+1] == "b":
                round += 1
                return round
            elif ls[i] == "b" and ls[i+1] == "a":
                round += 1
                return round
            if ls[i] == "a":
                win.append(ls[i])
            elif ls[i] == "b":
                win.append(ls[i])
            else:
                win.append(ls[i+1])
        round += 1
        ls = win
    return(round)