sword, heal, slimes, chest = False, False, True, True
room = 1

while True:
    if room == 1:
        print('Вы находитесь в пещере.')
        if not sword:
            print('Рядом с вами лежит меч. Напишите "взять" чтобы взять.')
        while room == 1:
            ans = input('Вы можете пойти вперёд, направо или налево.\n')
            if ans == 'взять':
                sword = True
                print('Вы подобрали меч.')  
            elif ans == 'вперёд':
                room = 3
            elif ans == 'налево':
                room = 2
            elif ans == 'направо':
                room = 4
    elif room == 2:
        print('Вы вышли в заросшую растительностью пещеру.')
        if not heal:
            print('Здесь растут ягоды. Говорят, они обладают целебными свойствами. ', end='') 
            print('Напишите "собрать" чтобы собрать их.')
        while room == 2:
            ans = input('Вы можете пойти назад.\n')
            if ans == 'собрать':
                heal = True
                print('Вы собрали ягоды.')  
            elif ans == 'назад':
                room = 1
    elif room == 3:
        print('Вы остановились на краю бездонной пропасти.')
        while room == 3:
            ans = input('Вы можете вырнуться в главную пещеру.\n')
            if ans == 'назад' or ans == 'вернуться':
                room = 1
    elif room == 4:
        print('Ход идёт вниз.')
        if not slimes:
            print('Без слизней эта пещера кажется странно пустой.')
            while room == 4:
                ans = input('Вы можете пойти вперёд или назад.\n')
                if ans == 'назад':
                    room = 1
                elif ans == 'вперёд':
                    room = 5
        else:
            print('На вас напали огромные пещерные слизни!')
            if sword:
                print('Вы можете сражаться или бежать.')
            else:
                print('Вам остаётся только бежать. (Требуется: меч)')
            while room == 4:
                ans = input('Что вы предпримете?\n')
                if ans == 'сражаться' and sword:
                    slimes = False
                    print('После тежёлой битвы вы победили этих монстров.')
                    if heal:
                        ans = input('Съесть ягоды, чтобы восстановить здоровье?\n')
                        if ans == 'да':
                            print('Вы сьели ягоды и восстановили здоровье.')
                            heal = False
                        else:
                            print('Лучше сохранить ягоды на всякий случай.')
                    ans = input('Вы можете вернуться назад или пойти дальше.\n')
                if ans == 'назад' or ans == 'бежать':
                    room = 1
                elif ans == 'дальше' or ans == 'вперёд':
                    room = 5
    elif room == 5:
        print('Вы вошли в древнюю сокровищницу.')
        print('Посреди пещеры стоит сундук.')
        if chest:
            print('Вы можете забрать драгоценности.')
            while room == 5:
                ans = input('Вы можете пойти назад или налево.\n')
                if ans == 'забрать':
                    print('Вы забрали все сокровища. Теперь сундук пуст.')
                    chest = False
                elif ans == 'назад':
                    room = 4
                elif ans == 'налево':
                    room = 2
        else:
            print('Он пуст.')
            while room == 5:
                ans = input('Вы можете пойти назад или налево.\n')
                if ans == 'назад':
                    room = 4
                elif ans == 'налево':
                    print('Проход скрыт за лианами. Неудивительно, что его ', end='')
                    print('невозможно обнаружить с другой стороны.')
                    room = 2