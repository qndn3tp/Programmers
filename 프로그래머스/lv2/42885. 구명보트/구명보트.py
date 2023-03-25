def solution(people, limit):
    n = 0
    people.sort(reverse=True)
    l = len(people)

    boat = []
    for i in range(0, len(people)-1):
        if i < len(people)-1 :

            if people[i] +  people[-1] <= limit:
                boat.append(people[i])
                boat.append(people[-1])
                n += 1
                people.pop()
    n += l-len(boat)
    return n