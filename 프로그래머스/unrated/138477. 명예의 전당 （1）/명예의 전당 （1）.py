def solution(k, score):
    table = []  # 정렬 후, 명예의 전당으로 관리
    ans = [] # 발표 점수
    for i in score:
        if len(table) < k:
            table.append(i)
            table_sorted = sorted(table, reverse=True)
            ans.append(table_sorted[-1])
        else:
            if table_sorted[-1] < i:
                table_sorted.pop()
                table_sorted.append(i)
                table_sorted = sorted(table_sorted, reverse=True)
                ans.append(table_sorted[-1])
            else:
                ans.append(table_sorted[-1])
    return ans