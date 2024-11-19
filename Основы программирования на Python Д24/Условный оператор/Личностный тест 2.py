season = input('Какое ваше любимое время года?\n')
if season == 'лето':
    ice_cream = input('Любите ли вы мороженое?\n')
    if ice_cream == 'да':
        print('Вы не любите ходить в школу и не любите жару')
    elif ice_cream == 'нет':
        print('Вы не любите ходить в школу и любите жару')
    else:
        print('Ошибка')
elif season == 'зима':
    tea = input('Любите ли вы горячий чай?\n')
    if tea == 'да':
        print('Вы любите согреваться после холодной улицы')
    elif tea == 'нет':
        print('Вы любите мороз')
    else:
        print('Ошибка')
elif season == 'осень' or season == 'весна':
    umbrella = input('Берёте ли вы с собой зонт?\n')
    if umbrella == 'да':
        print('Вы не любите дождь')
    elif umbrella == 'нет':
        print('Вы любите дождь')
    else:
        print('Ошибка')
else:
    print('Ошибка')