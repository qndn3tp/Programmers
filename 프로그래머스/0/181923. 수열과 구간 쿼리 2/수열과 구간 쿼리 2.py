def solution(arr, queries):
    ans = []
    for q in queries:
        res = -1
        ls = arr[q[0]:q[1]+1]
        ls = [i for i in ls if i > q[2]]
        if len(ls) == 0:
            ans.append(-1)
        else:
            ans.append(min(ls))

    return ans