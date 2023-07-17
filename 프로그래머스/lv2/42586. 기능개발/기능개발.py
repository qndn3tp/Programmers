def solution(progresses, speeds):
    # 기능별 필요한 작업의 일수    
    days = []
    for i in range(len(progresses)):
        n = (100 - progresses[i]) % speeds[i]
        if n == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append(((100 - progresses[i]) // speeds[i]) + 1)

    ans = []
    a = days[0]
    update = 0  # 개발할 수 있는 기능의 수
    for day in days:
        if day <= a:
            update += 1
        else:
            ans.append(update)
            a = day
            update = 1
    ans.append(update)

    return ans