def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]

    run = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        # 가장 우선순위일 경우  
        else:
            run += 1
            if cur[0] == location:
                break

    return(run)