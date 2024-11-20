import sys
input = sys.stdin.readline

def solution():
    start, end = 1, l-1

    res = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(len(store)-1):
            if store[i+1] - store[i] > mid:
                cnt += (store[i+1] - store[i] -1) // mid
        if cnt > m:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    return res

if __name__ == "__main__":
    n, m, l = map(int, input().rstrip().split())
    store = [0] + sorted(list(map(int, input().rstrip().split()))) + [l]
    print(solution())