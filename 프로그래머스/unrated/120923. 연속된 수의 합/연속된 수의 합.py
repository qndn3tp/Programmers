def solution(num, total):
    # 중간값
    mid_num = total // num

    # 중간값을 기준으로 더하고 빼야할 수의 개수
    n = num // 2

    if num % 2 == 1:
        start_num = mid_num - n
    else:
        start_num = mid_num - n + 1

    end_num = mid_num + n

    res = [i for i in range(start_num, end_num+1)]
    return res