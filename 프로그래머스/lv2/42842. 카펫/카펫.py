def solution(brown, yellow):
    #yellow 격자가 배치되는 모든 경우
    size = [] 
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            w, h = yellow // i, i
            if (w * 2) + (h * 2) + 4 == brown:
                return([w+2, h+2])