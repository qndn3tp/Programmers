def solution(array, commands):
    answer = []

    for c in range(len(commands)):
        answer.append(find_k(array, commands[c]))
    
    return answer

def find_k(arr, command):
    arr_ = arr[command[0]-1:command[1]]
    return sorted(arr_)[command[2]-1]