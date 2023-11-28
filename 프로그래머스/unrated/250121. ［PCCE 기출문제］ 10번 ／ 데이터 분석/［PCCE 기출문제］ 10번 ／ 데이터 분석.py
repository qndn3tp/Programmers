def solution(data, ext, val_ext, sort_by):
    keys = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    ext_key = keys[ext]   
    sort_key = keys[sort_by] 

    return sorted([d for d in data if d[ext_key] < val_ext], key = lambda x: x[sort_key])