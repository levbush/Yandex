s = input()
for i in range(0, len(s), 2):
    print(s)
    s = s[1:-1]
    if not s:
        break