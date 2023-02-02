def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        # 대문자
        if s[i].isupper():
            k = ord(s[i]) - ord('A') + n
            s[i] = chr(k % 26 + ord('A'))
        # 소문자
        elif s[i].islower():
            k = ord(s[i]) - ord('a') + n
            s[i] = chr(k % 26 + ord('a'))

    answer = "".join(s)
    return answer