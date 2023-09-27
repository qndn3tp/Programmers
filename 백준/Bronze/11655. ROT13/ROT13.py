import sys

s = sys.stdin.readline()

ans = ""
for char in s:
    if char.isupper():
        t = ord(char) + 13
        if t > 90:
            t -= 26
        ans += chr(t)
    elif char.islower():
        t = ord(char) + 13
        if t > 122:
            t -= 26
        ans += chr(t)
    else:
        ans += char
print(ans)