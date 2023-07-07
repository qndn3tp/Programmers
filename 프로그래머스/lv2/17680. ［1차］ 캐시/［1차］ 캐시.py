def solution(cacheSize, cities):
    # 대소문자 구분 없앰.
    cities = [city.lower() for city in cities]

    # 초기 캐시 설정 값. 
    t = 0
    queue = []

    for c in cities:
        if cacheSize == 0:
            t += 5
        elif len(queue) < cacheSize:    # 초기 캐시 채우기.
            if c in queue:
                i = queue.index(c)
                queue.pop(i)
                queue.append(c)
                t += 1
            else: 
                queue.append(c)
                t += 5
        else:                           # 캐시가 다 찼을 때.
            if c in queue:
                i = queue.index(c)
                queue.pop(i)
                queue.append(c)
                t += 1
            else:
                queue.pop(0)
                queue.append(c)
                t += 5
    return(t)