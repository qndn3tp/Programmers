import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

dic = {i:0 for i in b}
for i in b:
    ans = 1
    for j in b:
        if i > j:
            ans += 1
    dic[i] = ans

a.sort(reverse = True)

ans = 0
for i in b:
    if b.count(i) == 1:
        ans += i * a[dic[i]-1]
    # b에 중복이 있을 때 
    else:
        ans += i * a[dic[i]-1]
        dic[i] += 1
print(ans)