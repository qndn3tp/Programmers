def solution(s):
    ls = [int(i) for i in s.split()]
    ls.sort()
    return "%s %s" %(ls[0], ls[-1])