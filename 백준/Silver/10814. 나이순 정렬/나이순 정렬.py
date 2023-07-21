import sys

T = int(sys.stdin.readline())

data = []
for _ in range(T):
    data.append(sys.stdin.readline().strip().split(" "))

for d in data:    # 정렬시 lambda의 key가 문자열임. 정수로 고쳐 정수기준으로 정렬되도록함.
    d[0] = int(d[0])
data.sort(key = lambda data: data[0])    

for d in data:
    # print(d[0], d[1])
    age = d[0]
    name = d[1]
    print(f"{age} {name}")