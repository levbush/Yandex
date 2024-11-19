password = input()
if len(password) < 8:
    print('Короткий!')
elif '123' in password:
    print('Простой!')
elif input() != password:
    print('Различаются.')
else:
    print('OK')