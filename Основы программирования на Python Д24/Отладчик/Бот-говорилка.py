s = input().lower()
while 'пока' not in s and 'до свида' not in s:
    if ('не' in s and 'нет' not in s) or '?' in s:
        print('Напишите без не и без вопросительных знаков, пожалуйста')
    elif ('хорош' in s or 'прекрас' in s or 'отличн' in s) and ('плох' in s or 'ужас' in s or 'груст' in s):
        print('Какое у вас переменчивое настроение')
    elif 'хорош' in s or 'прекрас' in s or 'отличн' in s:
        print('Отлично, у меня тоже всё хорошо :)')
    elif 'плох' in s or 'ужас' in s or 'груст' in s:
        print('Ничего, всё наладится')
    elif 'норм' in s:
        print('Нормально - тоже хорошо!')
    elif 'привет' in s or 'здраств' in s:
        print('Привет! Рад тебя видеть!')
    elif '!' in s:
        print('Что же вы так кричите?')
    elif s.isdigit():
        print('Вы робот?')
    elif 'да' in s and 'нет' in s:
        print('Так да или нет?')
    elif 'да' in s:
        print('Рад, что вы со мной согласны')
    elif 'нет' in s:
        print('Жаль, что вы со мной не согласны')
    else:
        print('Я вас не понимаю')
    s = input().lower()
    if 'пока' in s or 'до свида' in s:
        print('Пока!')