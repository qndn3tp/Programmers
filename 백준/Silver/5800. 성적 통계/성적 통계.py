import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    score = list(map(int, sys.stdin.readline().split()))
    score.pop(0)
    score.sort(reverse=True)
    
    gap = 0
    for j in range(len(score)-1):
        if score[j] - score[j+1] >= gap:
            gap = score[j] - score[j+1]
    print("Class %d" %i)
    print("Max %d, Min %d, Largest gap %d" %(score[0], score[-1], gap))