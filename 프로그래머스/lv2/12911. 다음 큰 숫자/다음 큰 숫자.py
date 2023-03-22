def solution(n):
    cnt1 = bin(n).count("1")

    for i in range(n+1, 1000001):
        if bin(i).count("1") == cnt1:
            return(i)
            break
