import sys
input = sys.stdin.readline

def mettingSchedule():
    res = []
    meetings.sort(key=lambda x: (x[1], x[0]))

    for meeting in meetings:
        if len(res) == 0:
            res.append(meeting)
        else:
            if res[-1][1] <= meeting[0]:
                res.append(meeting)
    print(len(res))

if __name__ == "__main__":
    n = int(input().rstrip())
    meetings = []
    for _ in range(n):
        meetings.append(list(map(int, input().split())))
    mettingSchedule()