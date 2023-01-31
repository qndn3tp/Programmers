def solution(n, m):
    
    # 최대공약수 찾기 (for문의 감소 이용)
    for i in range(max(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break

    # 최소공배수 찾기
    for i in range(max(n,m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break

    return [gcd, lcm]