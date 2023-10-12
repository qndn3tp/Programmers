import sys

# 입력
nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline()))

# 최댓값, 위치 찾기
max_value = 0
index = 0
for idx, value in enumerate(nums):
    if value > max_value:
        max_value = value
        index = idx

# 출력
print(max_value)
print(index + 1)