import sys
input = sys.stdin.readline

def solution():
    left, right = pebbles[0], pebbles[1]
    for pebble in pebbles[2:]:
        if left == right:
            left += pebble
        else:
            if left > right:
                right += pebble
            else:
                left += pebble
    
    if left == right:
        return 0

    cnt = 0
    diff = max(left, right) - min(left, right)
    for c in chu:
        if diff < c:
            continue
        cnt += diff // c
        diff %= c
    return cnt

if __name__ == "__main__":
    _ = int(input().rstrip())            
    pebbles = list(map(int, input().split()))   
    chu = [100, 50, 20,10,5, 2, 1]
    print(solution())