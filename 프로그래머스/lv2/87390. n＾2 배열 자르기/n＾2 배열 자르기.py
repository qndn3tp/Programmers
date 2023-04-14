def solution(n, left, right):
    ls = []

    for i in range(left, right+1):
        ls.append(max(i//n+1, i%n+1))

    return(ls)