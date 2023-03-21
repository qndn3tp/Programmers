def solution(n):
    ls = [i for i in range(1, n//2+2)]

    cnt = 1
    for i in range(1, len(ls)): 
        sum = 0
        for j in range(i, len(ls)+1): 
            sum += j
            if sum == n:
                cnt += 1
                break
            elif sum > n:
                break
    return(cnt)