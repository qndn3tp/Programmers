def solution(s):

    res = 0
    for x in range(len(s)):
        ss = s[x:]
        ss += s[:x]
        
        stack = []
        for i in range(len(ss)):
            if ss[i] == "{" or ss[i] == "[" or ss[i] == "(":
                stack.append(ss[i])
            else:
                # if len(stack) > 0 and stack[-1] == ss[i]:
                #     stack.pop()
                if len(stack) > 0:
                    if ss[i] == "]" and stack[-1] == "[":
                        stack.pop()
                    if ss[i] == "}" and stack[-1] == "{":
                        stack.pop()
                    if ss[i] == ")" and stack[-1] == "(":
                        stack.pop()
                else:
                    stack.append(ss[i])
        if len(stack) == 0:
            res += 1
    return(res)