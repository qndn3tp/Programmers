# 소수인지 판별
def pn(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**1/2)+1):
            if n % i == 0:
                return False
    return True

from itertools import permutations
def solution(numbers):
    # 입력 문자열 => 각각의 숫자 리스트로
    nums = [int(numbers[i]) for i in range(len(numbers))]

    ans = []
    # 1자리 ~ n자리까지 순열 경우
    for i in range(1, len(nums)+1):     
        # 순열로 만들 수 있는 모든 경우
        perm = list(permutations(nums, i))      
        for j in range(len(perm)):
            num = int("".join(list(map(str, perm[j]))))
            # 소수 판별
            if pn(num):     
                ans.append(num)

    return len(list(set(ans)))