
def findGroupWord(s):
    ls = []
    for i in range(len(s)-1):
        if s[i] not in ls:
            ls.append(s[i])
        if s[i] != s[i+1] and s[i+1] in ls:
            return False
    return True

tc = int(input())
ans = 0
for _ in range(tc):
    word = input()
    if findGroupWord(word) == True:
        ans += 1
print(ans)