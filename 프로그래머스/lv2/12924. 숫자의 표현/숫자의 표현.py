def findFinn(n, idx):
    sum = 0
    for j in range(idx, n//2+2):
        sum += j
        if sum == n:
            return sum
        elif sum > n:
            break
    return 

def solution(n):
    cnt = 1
    for i in range(1, n//2+1):
        if findFinn(n, i) == n:
            cnt += 1
    return(cnt)