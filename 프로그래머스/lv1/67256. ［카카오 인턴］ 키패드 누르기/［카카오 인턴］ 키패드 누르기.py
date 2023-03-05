# 거리의 차 구하기 (n=와있는 곳, k=가야할 곳)
def find_distance(p, k):
    return abs(loc_dic[p][0]-loc_dic[k][0]) + abs(loc_dic[p][1]-loc_dic[k][1])



def solution(nums, hand):
    # 절대위치 dict 생성 (2차원 배열 이용)
    global loc_dic
    loc_dic = {}
    n = 1
    for i in range(3):
        for j in range(3):
            loc_dic[n] = (i,j)
            n += 1
    loc_dic["*"] = (3,0)
    loc_dic[0] = (3,1)
    loc_dic["#"] = (3,2)

    l_ls = [1, 4, 7]
    r_ls = [3, 6, 9]
    ls = [2, 5, 8, 0]

    r_visited = ["#"]
    l_visited = ["*"]

    res = []
    for n in nums:
        if n in r_ls:
            res.append("R")
            r_visited.append(n)
        elif n in l_ls:
            res.append("L")
            l_visited.append(n)
        else:
            # 바로 2,5,8,0이 나오는 경우 제외해야함
            if len(r_visited)==0 and len(l_visited)==0:
                if hand == "right":
                    res.append("R")
                    r_visited.append(n)
                else:
                    res.append("L")
                    l_visited.append(n)
                continue
            r_d = find_distance(r_visited[-1], n)
            l_d = find_distance(l_visited[-1], n)
            if l_d > r_d:
                res.append("R")
                r_visited.append(n)
            elif r_d > l_d:
                res.append("L")
                l_visited.append(n)
            else:
                if hand == "right":
                    res.append("R")
                    r_visited.append(n)
                else:
                    res.append("L")
                    l_visited.append(n)
    return("".join(res))

