def solution(bandage, health, attacks):
    attacks = sorted(attacks, reverse=True)

    t = 1           # 시간
    combo = 0       # 연속 성공
    hp = health     # 현재 체력
    
    while attacks:
        attack = attacks.pop()
        # 공격 시간이 안됐을 때
        if t != attack[0]:
            combo += 1
            #  체력 회복: 연속 성공
            if combo == bandage[0]:
                hp = min(hp+bandage[1]+bandage[2], health)
                combo = 0
            # 체력 회복: 연속 실패
            else:
                hp = min(hp+bandage[1], health)
            attacks.append(attack)
        # 공격시간이 됐을 때    
        else:
            # 체력 감소
            hp -= attack[1]
            if hp <= 0:
                return -1
            # 연속 실패
            combo = 0
        t += 1
    return hp