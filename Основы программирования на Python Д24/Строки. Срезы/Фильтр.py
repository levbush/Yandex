for i in range(int(input())):
    s = input()
    if s[:4] != '####':
        if s[:2] == '%%':
            s = s[2:]
        print(s)
