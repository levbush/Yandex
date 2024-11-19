password = input()
if len(password) < 8:
    print('Короткий!')
elif input() != password:
    print('Различаются.')
else:
    print('OK')