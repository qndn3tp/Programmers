def solution(files):
    ans = []
    for file in files:
        n, t = 0, 0
        change = True
        for i in range(len(file)):
            if file[i].isnumeric() and change:
                n = i
                change = False
                continue
            if file[i].isnumeric() == False and change == False:
                t = i
                break
        if t == 0:
            t = len(file)
        f = [file[:n], file[n:t], file[t:]]
        ans.append(f)

    ans = sorted(ans, key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(i) for i in ans]
