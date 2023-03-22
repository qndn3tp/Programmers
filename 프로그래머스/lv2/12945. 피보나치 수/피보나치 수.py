def solution(n):
    fibo = [0, 1]
    while len(fibo) <= n:
        fibo.append(fibo[-2]+fibo[-1])
    return(fibo[n]%1234567)