import sys

n = int(sys.stdin.readline())

stack = []
res = []

for _ in range(n):
    s = sys.stdin.readline().strip()

    if s == "top":
        if len(stack) > 0: res.append(stack[-1])
        else: res.append(-1)

    elif s == "size":
        res.append(len(stack))

    elif s == "empty":
        if len(stack) == 0: res.append(1)
        else: res.append(0)

    elif s == "pop":
        if len(stack) == 0: res.append(-1)
        else:
            res.append(stack[-1])
            stack.pop()
    # push
    else: stack.append(int(s[5:]))

for i in res:
    print(i)