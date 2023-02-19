def solution(s):
    dic = {}
    ans = []
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
            ans.append(-1)
        else:
            ans.append(i-dic[s[i]])
            dic[s[i]] = i
    return ans