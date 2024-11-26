s = set(input())
for i in s:
    if 65 <= ord(i) <= 90:
        print((i, ord(i) - 64))
    elif i == 'ё':
        print((i, 40))
    elif i == 'Ё':
        print((i, 7))
    elif 90 < ord(i) <= 122:
        print((i, ord(i) - 70))
    elif 1040 <= ord(i) <= 1071:
        print((i, ord(i) - 1040 + 1 + (1 if ord(i) > ord('Е') else 0)))
    elif 1072 <= ord(i) <= 1103:
        print((i, ord(i) - 1040 + 2 + (1 if ord(i) > ord('е') else 0)))