def solution(elements):
    numSet = set()

    cycle = elements * 2

    for i in range(len(elements)):
        for j in range(len(elements)):
            n = sum(cycle[i:i+j])
            numSet.add(n)
    return  len(numSet)