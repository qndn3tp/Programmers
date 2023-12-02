import sys

t = int(sys.stdin.readline())

for i in range(t):

    r, e, c = map(int, sys.stdin.readline().split())

    profit = e - c
    if r == profit:
        print("does not matter")
    elif r < profit:
        print("advertise")
    else:
        print("do not advertise")