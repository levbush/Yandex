n = int(input())
right = 0
while n > 0:
    if input() == 'раз':
        right += 1
    else:
        n -= 1
        print(f'Правильных отсчётов было {right}, но теперь вы ошиблись.')
        right = 0
        if n == 0:
            print('На сегодня хватит.')
            break
        continue
    if input() == 'два':
        right += 1
    else:
        n -= 1
        print(f'Правильных отсчётов было {right}, но теперь вы ошиблись.')
        right = 0
        if n == 0:
            print('На сегодня хватит.')
            break
        continue
    if input() == 'три':
        right += 1
    else:
        n -= 1
        print(f'Правильных отсчётов было {right}, но теперь вы ошиблись.')
        right = 0
        if n == 0:
            print('На сегодня хватит.')
            break
        continue
    if input() == 'четыре':
        right += 1
    else:
        n -= 1
        print(f'Правильных отсчётов было {right}, но теперь вы ошиблись.')
        right = 0
        if n == 0:
            print('На сегодня хватит.')
            break
        continue