# 소수인지 판별
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    # k진수로 만들기
    s = ""
    while n > 0:
        s += str(n % k)
        n //= k
    s = s[::-1]
    
    # 0의 인덱스 저장
    zero = []
    for i in range(len(s)):
        if s[i] == "0":
            zero.append(i)
            
    # 조건을 만족하는 소수 카운트
    s = s.split("0")

    ans = 0
    for i in s:
        if i == "":
            continue
        if isPrime(int(i)):
            ans += 1
    return ans