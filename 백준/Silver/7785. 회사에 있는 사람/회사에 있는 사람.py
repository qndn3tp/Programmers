import sys

n = int(sys.stdin.readline())

person = {}
for _ in range(n):
    log = sys.stdin.readline().split()
    if log[1] == "enter":
        person[log[0]] = 1
    else:
        person[log[0]] = 0

person = list(person.items())
person.sort(key = lambda x: x[0], reverse=True)

for key, value in person:
    if value != 0:
        print(key)