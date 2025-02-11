def solution(nums):
    n = len(nums) // 2
    cnt = len(set(nums))
    if cnt >= n:
        return n
    return cnt