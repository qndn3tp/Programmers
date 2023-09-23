def solution(name):
    spell_move = 0                  # 상-하 이동의 최솟값
    cursor_move = len(name) - 1     # 좌-우 이동의 최솟값

    for i, char in enumerate(name):
        spell_move += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)   # 상-하 이동의 최솟값(알파벳 변경 횟수)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 아래 3개의 경우 중 최솟값으로 갱신
        # 1. 좌->우로 방향을 바꾸지 않고 끝까지 가는 경우
        # 2. 연속된 A의 왼쪽 시작 (좌->우로 가다가 연속된 A를 만나면 되돌아감)
        # 3. 연속된 A의 오른쪽 시작 (좌<-우로 가다가 연속된 A를 만나면 되돌아감)
        cursor_move = min([ cursor_move, 2*i + len(name)-next, i + 2*(len(name)-next)])

    return spell_move + cursor_move