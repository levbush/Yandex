def ask_password():
    for _ in range(3):
        if input() == 'password':
            print('Пароль принят')
            return
    print('В доступе отказано')