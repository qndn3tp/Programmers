
def findCroAlpha(s):
    cro_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for i in cro_alpha:
        s = s.replace(i, "#")
    return len(s)

t = input()
print(findCroAlpha(t))