# 날짜 형식을 모두 day로 바꿈
def dateToDays(date):
    y = int(date[:4])
    m = int(date[5:7])
    d = int(date[8:10])

    days = (y * 28 * 12) + (m * 28) + d
    return days

def solution(today, terms, privacies):
    t_dict = {}
    for t in terms:
        t_dict[t[0]] = t[2:]

    p = [p.split(" ") for p in privacies]

    # 데이터를 보기 쉬운 구조로 고침.
    for i in p:
        i[1] = t_dict[i[1]]

    res_days = [dateToDays(date[0]) + int(date[1]) * 28 for date in p]

    ans = []
    for i in range(len(res_days)):
        if res_days[i] <= dateToDays(today):
            ans.append(i+1)
    
    return ans