def solution(phone_book):
    pb = sorted(phone_book)
    
    for i in range(len(pb)-1):
        l = len(pb[i])
        if pb[i+1][:l] == pb[i]:
            return False
    return True