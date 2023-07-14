import sys

n = int(sys.stdin.readline())

input_list = [sys.stdin.readline().strip() for _ in range(n)]

for s in input_list:
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")