n1 = int(input())
n2 = input()
ans = []
for i in range(len(n2)):
    n = n2[len(n2)-1-i]
    ans.append(n1 * int(n))

# 세자리 수 곱셈 결과값
res = 0
for i in range(3):
    res += ans[i] * 10**i
ans.append(res)

for num in ans:
    print(num)