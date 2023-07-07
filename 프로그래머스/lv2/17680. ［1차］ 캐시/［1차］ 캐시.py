def solution(cacheSize, cities):
    # 대소문자 구분 없앰.
    cities = [city.lower() for city in cities]

    # 초기 캐시 설정 값. 
    t = 0
    queue = []

    for c in cities:
        if cacheSize == 0:
            t += 5
        else:                          
            if c in queue:
                i = queue.index(c)
                queue.pop(i)
                queue.append(c)
                t += 1
            else:
                if len(queue) >= cacheSize: # 캐시가 다 찼을 때만 pop().
                    queue.pop(0)
                queue.append(c)
                t += 5
    return(t)
