def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days30 = [4, 6, 9, 11]
    total_days = 0
    for i in range(1, a):
        if i == 2:
            total_days += 29
        elif i in days30:
            total_days += 30
        else:
            total_days += 31
    total_days += b
    return day[(total_days - 1) % 7]