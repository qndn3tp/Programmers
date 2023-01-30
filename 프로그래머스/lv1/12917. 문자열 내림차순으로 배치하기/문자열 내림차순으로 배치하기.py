def solution(s):
    
    ls = [ord(i) for i in s]
    ls.sort(reverse=True)
    
    ls = [chr(i) for i in ls]
    answer = "".join(ls)
    
    return answer