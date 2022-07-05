print('Введите своё имя')
name = input()
name = name + '.'
rank = 0
action = ''
secsim = []
numbers = []
num_in_secsim = None
for i in range(1, 34):
    if i < 10:
        numbers.append('0' + str(i))
    else:
        numbers.append(str(i))
digits = [j for j in range(10)]
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text_encrypted = ''
text_num = ''
text_decrypted = ''
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
        print('Введите название действия, которое вы хотите сделать. Возможные действия: "Шифр", "Ввод secsim", "Выход"')
        action = input()
        if action == 'Ввод secsim':
            if rank == 3:
                for _ in range(10):
                    secsim.append(input())
            else:
                print('Вам не разрешено выполнять это действие')
        if action == 'Шифр':
            print('Расшифровка или Зашифровка?')
            action = input()
            if action == 'Расшифровка':
                print('Введите текст')
                text_encrypted = input()
                for n in range(len(text_encrypted)):
                    num_in_secsim = secsim.find(text_encrypted[n])
                    text_num = digits.find(num_in_secsim)
                for m in range(len(text_num)):
                    text_num += (digits[digits.find(text_num[m])])