import sys
ans = 0

n, k = map(int, sys.stdin.readline().split())

need = k * (k+1) // 2   # 문제의 조건을 만족하기 위해 필요한 최소 공의 개수 (1씩 증가하는 등차수열의 합)

if n < need:    # 이것보다 부족하면 조건을 만족하지 못함.
    ans = -1
else:
    if (n - need) % k == 0:   # 위와 같은 등차수열 메커니즘
        ans = k - 1
    else:   # 아니라면 오른쪽(큰 수)부터 1씩 담음.
        ans = k     
print(ans)