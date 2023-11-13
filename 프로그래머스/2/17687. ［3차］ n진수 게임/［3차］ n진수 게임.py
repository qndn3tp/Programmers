# 10진수 -> n진수 
def convertToN(a, b):   # 10진수 a를 b진수로 바꿈
    alpha = ["A", "B", "C", "D", "E", "F"]
    res = ""
    while a > 0:
        a, mod = divmod(a, b)
        if mod > 9:
            res += alpha[mod-10]
        else:
            res += str(mod)
    return res[::-1]

def solution(n, t, m, p):
    nums = "0"
    num = 1
    while len(nums) <= (m * t):
        nums += convertToN(num, n)
        num += 1

    res = ""
    for i in range(p-1, m*t, m):
        res += nums[i]
    return res