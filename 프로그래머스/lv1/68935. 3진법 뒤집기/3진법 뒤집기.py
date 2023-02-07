def solution(n):
    # 앞 뒤 반전(3진법)
    trit = []
    while n > 0:
        trit.append(n % 3)
        n //= 3
    # 다시 10진법
    dec = 0
    trit = trit[::-1]
    for i in range(len(trit)):
        if trit[i] != 0:
            dec += trit[i] * (3 ** i)
    return dec