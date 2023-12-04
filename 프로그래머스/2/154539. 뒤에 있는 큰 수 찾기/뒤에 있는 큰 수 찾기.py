def solution(numbers):
    ans = [-1] * len(numbers)

    # 뒷큰수가 필요한 인덱스 저장(stack에 남아있는 인덱스는 뒷큰수를 발견 못함)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            ans[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)

    return ans