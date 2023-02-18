def solution(arr, divisor):
    ans = []
    for i in arr:
        if i % divisor == 0:
            ans.append(i)
    if ans:
        return(sorted(ans))
    else:
        return([-1])
