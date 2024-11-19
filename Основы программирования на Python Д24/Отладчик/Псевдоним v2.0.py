num = int(input())
turn = 0
while num > 0:
    turn += 1
    if turn % 2:
        if num < 4:
            n = num
        elif num % 4:
            n = num % 4
        else:
            n = 1
        num -= n
        print(n, num)
        if num == 0:
            print('ИИ выиграл!')
    else:
        n = int(input())
        while n > 3 or n < 1 or n > num:
            print('Некорректный ход:', n)
            n = int(input())
        num -= n
        print(n, num)
        if num == 0:
            print('Вы выиграли!')
            

# 0 4 8
# 1 2 3 5 6 7