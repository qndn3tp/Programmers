import sys
from itertools import combinations

# 입력 
height = []
for i in range(9):
    height.append(int(sys.stdin.readline()))

# 난쟁이가 아닌 사람 찾기
comb = combinations(height, 2)
for i in comb:
    if sum(height) - (i[0] + i[1]) == 100:
        ans = [i[0], i[1]]

# 출력 
height = sorted([i for i in height if i not in ans])
for i in height:
    print(i)