def solution(numbers):
    res = []
    for n in numbers:
        # 짝수의 경우 첫자리 비트만 1로 바꾸면 됨
        if n % 2 == 0:
            res.append(n+1)
        # 홀수일 경우
        else:
            bn = list("0" + bin(n)[2:])
            idx = (len(bn) - 1) - bn[::-1].index("0")
            bn[idx] = "1"
            bn[idx + 1] = "0"
            res.append(int("".join(bn), 2))
    return res
