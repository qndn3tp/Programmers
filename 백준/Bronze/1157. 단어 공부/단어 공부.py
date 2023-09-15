import sys
from collections import Counter

s = sys.stdin.readline().strip().upper()    # 대문자로 출력하기위해 전처리
s = " ".join(s).split(" ")                  # 문자열 -> 알파벳 각각을 리스트로
c = Counter(s)

res = c.most_common(1)[0][1]                # 최빈값으로 내림차순 정렬. 첫번째 원소의 빈도수

most_used = []                              # 가장 많이 사용된 알파벳 저장
for i in c:
    if c[i] == res: 
        most_used.append(i)
print(most_used[0] if len(most_used)==1 else "?")