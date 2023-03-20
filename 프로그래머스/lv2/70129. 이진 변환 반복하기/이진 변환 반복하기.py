def binTrans(x):
    x_deleted = x.replace("0", "")
    return bin(len(x_deleted))[2:], len(x) - len(x_deleted) # 제거한 0의 개수 => 0 제거 전 문자열의 길이 - 제거 후 길이

def solution(s):
    n_del0 = 0        # 제거 된 총 0의 개수
    n_trans = 0       # 이진변환 횟수

    while len(s) > 1:
        n_trans += 1
        s, n_del = binTrans(s) 
        n_del0 += n_del

    return([n_trans, n_del0])