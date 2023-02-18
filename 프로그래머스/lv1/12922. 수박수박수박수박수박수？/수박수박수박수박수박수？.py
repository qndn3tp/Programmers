def solution(n):
    answer = ''
    s = ["수", "박"]
    for i in range(n):
        answer += s[i%2]
    return answer