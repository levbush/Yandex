print('Введите своё имя')
name = input()
name = name + '.'
rank = 0
action = ''
secsim = ['с', 'к', 'о', 'м', 'п', 'ь', 'ю', 'т', 'е', 'р']
numbers = []
for i in range(1, 34):
    if i < 10:
        numbers.append('0' + str(i))
    else:
        numbers.append(str(i))
digits = [str(j) for j in range(10)]
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text_encrypted = ''
text_num = ''
text_decrypted = ''
print('Введите пароль')
password = input()
if password == ''.join(['e', 'm', 'p', 'e', 'e']):
    print('Здравствуйте, сотрудник', name)
    rank = 1
elif password == ''.join(['h', 'o', 'n', 'o', 'm', 'e', 'm']):
    print('Здравствуйте,', name, 'Для Вас доступны привилегии почётного члена команды')
    rank = 2
elif password == ''.join(['h', 'i', 'g', 'e', 's', 's']):
    print('Здравствуйте,', name, 'Для Вас активирован высший доступ')
    rank = 3
else:
    print('Здравствуйте,', name, 'Вы ошиблись, либо вас сдесь не должно быть')
if rank != 0:
    while action != 'Выход':
        print('Введите название действия, которое вы хотите сделать. Возможные действия: "Шифр", "Выход"')
        action = input()
        if action == 'Шифр':
            print('Расшифровка или Зашифровка?')
            action = input()
            if action == 'Расшифровка':
                print('Введите текст')
                text_encrypted = input()
                for n in range(len(text_encrypted)):
                    text_num += digits[secsim.index(text_encrypted[n])]
                for m in range(0, len(text_num), 2):
                    text_decrypted += letters[numbers.index(text_num[m] + text_num[m + 1])]
                print(text_decrypted)