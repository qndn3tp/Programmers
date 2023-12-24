def solution(ineq, eq, n, m):
    if eq == "=":
        s = str(n) + ineq + eq + str(m)
    else:
        s = str(n) + ineq + str(m)
    return 1 if eval(s) else 0