import sys
input = sys.stdin.readline

def binarySearch(a, b):
    res = 0
    for i in range(len(a)):
        l, r = 0, len(b)-1
        while l <= r:
            mid = (l + r )// 2
            if a[i] <= b[mid]:
                r = mid - 1
            elif a[i] > b[mid]:
                res += mid - l + 1
                l = mid + 1
    print(res)

if __name__ == "__main__":
    t = int(input().rstrip())
    for _ in range(t):
        an, bn = map(int, input().rstrip().split())

        A = list(map(int, input().strip().split()))
        B = sorted(list(map(int, input().strip().split())))

        binarySearch(A, B)