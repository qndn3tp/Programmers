# 최대공약수 찾기 
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 찾기 
def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    l = lcm(denom1, denom2)

    # 분수 덧셈을 위해 곱해야할 값
    d1 = l // denom1
    d2 = l // denom2

    res = [numer1 * d1 + numer2 * d2, l]

    # 기약분수
    cd = gcd(res[0], res[1])

    res = [res[0] // cd, res[1] // cd]
    return res