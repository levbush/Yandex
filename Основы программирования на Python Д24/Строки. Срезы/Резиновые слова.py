if len(s := input()) % 2 == 1:
    lens = len(s) // 2
    spaces = ' ' * lens
    for i in range(lens, -1, -1):
        if i == lens:
            print(spaces + s[i])
        else:
            print(spaces + s[i] + ' ' * ((lens - len(spaces)) * 2 - 1) + s[-(i + 1)])
        spaces = spaces[:-1]
else:
    lens = (len(s) - 1) // 2
    spaces = ' ' * lens
    for i in range(lens, -1, -1):
        print(spaces + s[i] + ' ' * ((lens - len(spaces)) * 2) + s[-(i + 1)])
        spaces = spaces[:-1]