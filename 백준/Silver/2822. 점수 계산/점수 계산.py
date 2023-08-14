import sys

score = [int(sys.stdin.readline()) for _ in range(8)]
score = [[i+1, v] for i, v in enumerate(score)]
score.sort(key = lambda x:x[1], reverse=True)
score = score[:5]

sum_ = sum([s[1] for s in score])
print(sum_)
num_ = " ".join(map(str, sorted([s[0] for s in score])))
print(num_)