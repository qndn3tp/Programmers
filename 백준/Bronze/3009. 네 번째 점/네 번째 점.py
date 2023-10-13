import sys

# 입력
x_nums = {}
y_nums = {}
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x in x_nums:
        x_nums[x] += 1
    elif x not in x_nums:
        x_nums[x] = 1
    if y in y_nums:
        y_nums[y] += 1
    elif y not in y_nums:
        y_nums[y] = 1

# 네 번째 점 찾기
x_nums = sorted(x_nums.items(), key=lambda x: x[1])
y_nums = sorted(y_nums.items(), key=lambda x: x[1])

# 출력
print(x_nums[0][0], y_nums[0][0])