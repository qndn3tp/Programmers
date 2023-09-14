import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
    
    else:
        f, x = temp[0], temp[1]
        x = int(x)

        if f == "add":
            s.add(x)
        elif f == "remove":
            s.discard(x)
        elif f == "check":
            print(1 if x in s else 0)
        elif f == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)