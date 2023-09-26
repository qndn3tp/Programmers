from collections import deque

def solution(prices):
    prices = deque(prices)	
    ans = []

    while prices:
        price = prices.popleft()
        keep = 0                    # 가격이 떨어지지 않은 기간

        # 마지막 가격인 경우(가격이 떨어지지 않은 기간이 0초)
        if len(prices) == 0:
            ans.append(0)
            break

        # 위의 경우가 아닌 경우(직접 비교)
        for i in prices:
            keep += 1
            if price > i:   # 가격이 떨어졌다면
                break               # 가격이 떨어졌기 때문에 종료   
        ans.append(keep)

    return ans