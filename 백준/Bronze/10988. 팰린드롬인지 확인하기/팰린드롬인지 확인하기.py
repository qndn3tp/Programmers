import sys

# 입력
s = sys.stdin.readline().strip()

# 팰린드롬 찾기
idx = (len(s) // 2)   # 비교해야하는 인덱스

ans = 1
for i in range(idx):
    if s[i] == s[len(s)-i-1]:
        continue
    else:
        ans = 0
        break
# 출력
print(ans)