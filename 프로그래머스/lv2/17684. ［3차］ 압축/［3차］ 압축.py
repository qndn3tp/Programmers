# 1번 
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for i in range(len(alphabet)):
    dic[alphabet[i]] = i+1

def solution(s):
    res = []    # 출력할 결과
    new_idx = 27

    while len(s) > 0:
        # 2번 
        for i in range(len(s)):
            if s[:i+1] in dic:
                word = s[:i+1]
        if not word:
            break
        # 3번
        res.append(dic[word])
        s = s[len(word):]
        # 4번
        if len(s) > 0:
            new = word + s[0]
            dic[new] = new_idx
            new_idx += 1

    return res