from collections import Counter

def solution(topping):
    # 철수가 가진 토핑의 종류, 동생이 가진 토핑의 종류
    A, B = set(), Counter(topping)

    # 철수가 가진 토핑의 개수, 동생이 가진 토핑의 개수
    a, b = 0, len(B)

    ans = 0
    for t in topping:
        # 동생이 가진 토핑에서 해당 토핑의 개수 -1 (= 형이 가짐)
        B[t] -= 1

        # 동생이 해당 토핑을 가지고 있지 않다면, 동생이 가진 토핑의 종류 -1
        if B[t] == 0:
            b -= 1

        # 철수가 해당 토핑을 갖고 있지 않다면, 철수가 가진 토핑의 종류에 추가 후 토핑의 종류 +1
        if t not in A:
            A.add(t)
            a += 1

        # 철수가 가진 토핑의 종류와 동생이 가진 토핑의 종류가 같은 경우
        if a == b:  
            ans += 1 

        # 이후 연산은 불필요
        if a > b:
            break
    return ans