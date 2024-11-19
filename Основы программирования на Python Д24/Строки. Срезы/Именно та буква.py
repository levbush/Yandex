s, i, n = input(), int(input()), input()
if len(n) > 1 or i > len(s) or i < 1:
    print('ОШИБКА')
elif s[i - 1] == n:
    print('ДА')
else:
    print('НЕТ')