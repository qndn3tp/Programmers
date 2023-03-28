def find_lcm(a,b):  
    ls_a = [a*i for i in range(1, b+1)]
    ls_b = [b*i for i in range(1, a+1)]

    for n in ls_a:
        if n in ls_b:
            return n

def solution(arr):
    while len(arr) > 1:
        n = find_lcm(arr[0],arr[1])
        arr = arr[1:]
        arr[0] = n

    return(arr[0])
    