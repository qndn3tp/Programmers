def solution(record):
    people = {}
    for r in record:
        if r[0] != "L":
            state, id, name = r.split()
            people[id] = name

    res = []
    for r in record:
        data = r.split()
        if data[0] == "Enter":
            res.append("{}님이 들어왔습니다.".format(people[data[1]]))
        elif data[0] == "Leave":
            res.append("{}님이 나갔습니다.".format(people[data[1]]))
    return res