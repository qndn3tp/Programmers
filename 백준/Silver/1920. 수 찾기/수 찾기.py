import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in arr:
    left, right = 0, len(a)-1
    isFind = False

    # 이분탐색
    while left <= right:
        mid = (left + right) // 2
        
        # 중간값이 타겟값일 때, break
        if i == a[mid]:
            isFind = True
            print("1")
            break
        # 중간값보다 클 때, left 옮김
        elif i > a[mid]:
            left = mid + 1
        # 중간값보다 작을 때, right를 옮김
        else:
            right = mid - 1
    if not isFind:
        print("0")