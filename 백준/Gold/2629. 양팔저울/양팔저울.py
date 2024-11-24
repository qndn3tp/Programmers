import sys
input = sys.stdin.readline

def solution():
    # 가능한 모든 무게를 기록할 dp 배열 (0부터 max_chu까지)
    dp = [False] * (max_chu + 1)
    dp[0] = True  # 0 무게는 항상 가능

    for weight in chu:
        # 기존 dp 배열의 값을 기반으로 갱신하기 위해 임시 배열을 사용
        temp = dp[:]
        for j in range(max_chu + 1):
            if dp[j]:
                if j + weight <= max_chu:  # 무게를 추가한 경우
                    temp[j + weight] = True
                temp[abs(j - weight)] = True  # 무게 차이를 사용한 경우
        dp = temp

    # 결과 확인
    res = []
    for marble in marbles:
        # 구슬의 무게가 max_chu를 초과하면 불가능
        if marble > max_chu:
            res.append("N")
        elif dp[marble]:
            res.append("Y")
        else:
            res.append("N")

    print(*res)


if __name__ == "__main__":
    _ = int(input().rstrip())  # 추의 개수
    chu = list(map(int, input().split()))  # 추의 무게
    max_chu = sum(chu)  # 가능한 최대 무게
    __ = int(input().rstrip())  # 구슬의 개수
    marbles = list(map(int, input().split()))  # 구슬의 무게

    solution()
