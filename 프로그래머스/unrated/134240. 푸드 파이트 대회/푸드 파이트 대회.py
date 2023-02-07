def solution(food):
    ans = ""

    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            ans += str(i)
    ans += "0" # 물
    ans = ans+ans[:-1][::-1]
    
    return ans