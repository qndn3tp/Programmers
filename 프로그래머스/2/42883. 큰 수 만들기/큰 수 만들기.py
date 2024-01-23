def solution(number, k):
    stack = []
    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
            continue
        if k > 0:
            while stack[-1] < number[i]:
                stack.pop()
                k -= 1
                if len(stack) == 0 or k == 0:
                    break
        stack.append(number[i])
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)