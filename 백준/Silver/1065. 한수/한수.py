
import sys
nums = int(sys.stdin.readline())

# 한수인지 판별하는 함수
def solution(n):
    for i in range(1,len(n)-1):
        if 2 * int(n[i]) != int(n[i-1]) + int(n[i+1]):
            return 0
    return 1

ans = 0
for num in range(1, nums+1):
    # 1,2자리 숫자는 무조건 한수
    if len(str(num)) <= 2:
        ans += 1
    # 3자리 이상은 검사
    else:
        if solution(str(num)) == 1:
            ans += 1
print(ans)


