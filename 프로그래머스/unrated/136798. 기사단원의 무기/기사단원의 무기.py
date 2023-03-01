import math
# 약수의 개수
def div_num(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 1
    if math.sqrt(n) % 1 == 0:
        return cnt*2 - 1
    else:
        return cnt*2
def solution(number, limit, power):
    n = [div_num(i) for i in range(1,number+1)]
    ans = 0
    for i in n:
        if i <= limit:
            ans += i
        else:
            ans += power
    return(ans)
