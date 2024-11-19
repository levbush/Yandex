num1, num2 = int(input()), int(input())
turn = 0
num = None
while num1 > 0 or num2 > 0:
    turn += 1
    if turn % 2:
        n1 = abs(num1 - num2)
        if num1 > num2:
            num1 -= n1
            print('Куча 1 =', num1, 'Взято', n1)
        elif num1 < num2:
            num2 -= n1
            print('Куча 2 =', num2, 'Взято', n1)
        else:
            num1 -= 1
            n1 = 1
            print('Куча 1 =', num1, 'Взято', n1)
        if num1 == 0 and num2 == 0:
            print('ИИ выиграл!')
    else:
        if num1 > 0 and num2 > 0:
            while num != 1 and num != 2:
                num = int(input('Введите номер кучи (1 или 2)\n'))
                if num == 1:
                    n2 = int(input('Сколько камней забрать?\n'))
                    while n2 > num1 or n2 < 1:
                        print('Некорректный ход:', n2)
                        n2 = int(input('Сколько камней забрать?\n'))
                    num1 -= n2
                    print('Куча 1 =', num1, 'Взято', n2)
                elif num == 2:
                    n2 = int(input('Сколько камней забрать?\n'))
                    while n2 > num2 or n2 < 1:
                        print('Некорректный ход:', n2)
                        n2 = int(input('Сколько камней забрать?\n'))
                    num2 -= n2
                    print('Куча 2 =', num2, 'Взято', n2)
        elif num1 > 0:
            while num != 1:
                num = int(input('Введите номер кучи (1)\n'))
                if num == 1:
                    n2 = int(input('Сколько камней забрать?\n'))
                    while n2 > num1 or n2 < 1:
                        print('Некорректный ход:', n2)
                        n2 = int(input('Сколько камней забрать?\n'))
                    num1 -= n2
                    print('Куча 1 =', num1, 'Взято', n2)
        elif num2 > 0:
            while num != 2:
                num = int(input('Введите номер кучи (2)\n'))
                if num == 2:
                    n2 = int(input('Сколько камней забрать?\n'))
                    while n2 > num2 or n2 < 1:
                        print('Некорректный ход:', n2)
                        n2 = int(input('Сколько камней забрать?\n'))
                    num2 -= n2
                    print('Куча 1 =', num2, 'Взято', n2)
        if num1 == 0 and num2 == 0:
            print('Вы выиграли!')
        num = None
# 0 0 W
# 0 1 L
# 1 1 W
# 1 2 L
# 2 2 W
# 2 3 L
# 1 3 L
# 3 3 W
# 0 2 L
# 0 3 L