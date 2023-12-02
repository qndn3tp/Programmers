import math

def solution(fees, records):
    # 요금표
    default_time, default_fee, unit_time, unit_fee = fees
    
    table = {}          # 차 번호: 각 주차 시간 계산(입출차 체크용)
    using_time = {}     # 차 번호: 총 주차 시간
    for i in records:
        time, number, io = i.split(" ")     # 시각, 차량번호, 내역
        h, m = time.split(":")
        mm = 60 * int(h) + int(m)

        if io == "IN":                  # 입차 시 입차 시간 기록
            table[number] = mm          

        elif io == "OUT":               # 출차 시 사용시간 계산, 입차 기록 삭제
            if number not in using_time:    
                using_time[number] = mm - table[number]
            else:
                using_time[number] += (mm - table[number])
            del table[number]

    # 마지막까지 출차가 안된 차
    for k, v in table.items():
        if k in using_time:
            using_time[k] += (60 * 23 + 59) - v 
        else:
            using_time[k] = (60 * 23 + 59) - v 

    using_time = sorted(list(using_time.items()), key = lambda x: x[0])     # 차 번호로 정렬

    res = []
    for i in using_time:
        cost = default_fee
        if i[1] <= default_time:    # 기본 시간보다 적은 경우 
            res.append(cost)    
        else:                       # 기본 시간보다 많은 경우
            cost += math.ceil((i[1] - default_time) / unit_time) * unit_fee     # 올림
            res.append(cost)
    return res