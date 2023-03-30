nums = [i for i in range(1,10001)]
self_nums = []

for num in nums:
    res = num
    for i in str(num):
        res += int(i)
    self_nums.append(res)

ans = list(set(nums)-set(self_nums))
ans.sort()
for n in ans:
    print(n)