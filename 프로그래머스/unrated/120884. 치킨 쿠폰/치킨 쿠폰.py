def solution(chicken):
    coupon = 0
    res = 0
    while chicken > 0:
        chicken -= 1
        coupon += 1
        if coupon == 10:
            chicken += 1
            res += 1
            coupon = 0

    return res