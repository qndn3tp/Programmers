import collections
def solution(X, Y):
    x = list(X)
    y = list(Y)
    dict_x = collections.Counter(x)
    dict_y = collections.Counter(y)
    res = ""
    for k, v in sorted(dict_x.items(), reverse=True):
        if k in dict_y:
            res += k * min(dict_x[k], dict_y[k])
    if len(res) == 0:
        return "-1"
    elif res[0] == "0":
        return "0"
    else:
        return(res)
