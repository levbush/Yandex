print('Введите своё имя')
name = input()
name = name + '.'
rank = 0
action = ''
print('Введите пароль')
password = input()
if password == 'empee':
    print('Здравствуйте, сотрудник', name)
    rank = 1
elif password == 'honomem':
    print('Здравствуйте,', name, 'Для Вас доступны привилегии почётного члена команды')
    rank = 2
elif password == 'higess':
    print('Здравствуйте,', name, 'Для Вас активирован высший доступ')
    rank = 3
else:
    print('Здравствуйте,', name, 'Вы ошиблись, либо вас сдесь не должно быть')
if rank != 0:
    while action != 'Выход':
        print('Введите название действия, которое вы хотите сделать. Возможные действия: "Шифр1", "Шифр2", "Выход"')
        action = input()
        if action == 'Шифр1':
            print('Расшифровка или Зашифровка?')
            action = input()
            if action == 'Зашифровка':
                print('Введите слово (с разделом на слога символом "|")')
                word = input().split('|')
                last_syllable = word[-1]
                del word[-1]
                word.insert(0, last_syllable)
                print(*word, sep='')
            if action == 'Расшифровка':
                print('Введите слово (с разделом на слога символом "|")')
                word = input().split('|')
                last_syllable = word[0]
                del word[0]
                word.append(last_syllable)
                print(*word, sep='')