# 10진수 to 2진수
def decToBin(num, n):
    bin_n = []
    while num > 0:
        bin_n.append(num % 2)
        num //= 2

    # 이진수 변환 후 길이 맞추기
    while len(bin_n) < n:
        bin_n.append(0) 
    bin_n = bin_n[::-1]

    return bin_n

def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    map_ = map1
    
    # 각각 지도 생성
    for i in arr1:
        map1.append(decToBin(i, n))
    for i in arr2:
        map2.append(decToBin(i, n))
        
    # 지도 두 개 병합
    for r in range(n):
        for c in range(n):
            if map1[r][c] == 0 and map2[r][c] == 0:
                map_[r][c] = 0
            else:
                map_[r][c] = 1
                
    # 지도 해독
    secret_map = []
    for r in range(n):
        secret = ""
        for c in range(n):
            if map_[r][c] == 1:
                secret += "#"
            else:
                secret += " "
        secret_map.append(secret)

    return secret_map
