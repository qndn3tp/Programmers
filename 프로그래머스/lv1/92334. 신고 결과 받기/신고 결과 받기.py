def solution(id_list, report, k):
    rp = [user.split(" ") for user in set(report)]


    # 신고받은 이용자 리스트(id-신고당한 횟수)
    dic = {}
    for id in id_list:
        dic[id] = 0
    for rp_user in rp:
        if rp_user[1] in dic:
            dic[rp_user[1]] += 1
    
    # 정지되야할 이용자
    banned = []
    for i in dic:
        if dic[i] >= k:
            banned.append(i)
            
    # 유저id-유저가 신고한id
    user_dic = {}
    for user in rp:
        if user[0] not in user_dic:
            user_dic[user[0]] = [user[1]]
        else:
            if user[1] not in user_dic[user[0]]:
                user_dic[user[0]].append(user[1])

    # 결과
    res = {}
    for i in id_list:
        res[i] = 0
    for rp_user in rp:
        if rp_user[1] in banned:
            res[rp_user[0]] += 1

    return(list(res.values()))