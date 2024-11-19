s = input()
if 'не' in s.lower() or '?' in s:
    print('Я вас не понимаю')
elif 'хорош' in s.lower() or 'прекрас' in s.lower() or 'отличн' in s.lower():
    print('Отлично, у меня тоже всё хорошо :)')
elif 'плох' in s.lower() or 'ужас' in s.lower():
    print('Ничего, всё наладится')
else:
    print('Я вас не понимаю')