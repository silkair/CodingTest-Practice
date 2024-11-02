def solution(bandage, health, attacks):

    t, x, y = bandage
    max_health = health
    current_health = health
    heal_success = 0
    attack_time = 0
    time = 0
    answer = 0 #현재 체력

    while time <= attacks[-1][0]:  # 마지막 공격 시간까지
        # 현재 시간이 공격 시간에 해당하면 체력을 감소시킨다
        if attack_time < len(attacks) and time == attacks[attack_time][0]:
            damage = attacks[attack_time][1]
            current_health = current_health - damage
            heal_success = 0  # 공격받으면 연속 성공 초기화
            attack_time += 1
            if current_health <= 0:  # 체력이 0 이하이면 게임 오버
                return -1
        else:
            # 공격받지 않은 경우 체력을 회복한다
            if heal_success < t:
                current_health += x
                heal_success += 1
                if current_health > max_health:
                    current_health = max_health
            # t초 동안 성공적으로 붕대를 감으면 추가 회복
            if heal_success == t:
                current_health += y
                if current_health > max_health:
                    current_health = max_health
                heal_success = 0  # 연속 성공 초기화

        answer = current_health  # 남은 체력을 answer에 저장
        time += 1

    return answer