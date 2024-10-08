import sys
input = sys.stdin.readline

def main() :
    n = int(input().strip())
    a = list(map(int, input().split()))

    a_dict = {}
    for i in range(len(a)):
        if a[i] not in a_dict:
            a_dict[a[i]] = [i]
        else:
            a_dict[a[i]].append(i)

    b = sorted(a)

    p = [0 for _ in range(n)]

    for i in range(len(b)):
        num = b[i]
        idx = a_dict[num][0]
        a_dict[num].pop(0)
        p[idx] = i

    print(*p)

if __name__ == '__main__':
    main()