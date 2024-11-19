s, n = input(), int(input())
if n < 1 or n > len(s):
    print('ОШИБКА')
else:
    print(s[n - 1])