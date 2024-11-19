alphabet = [chr(i) for i in range(97, 123)]


def f():
    for el in input():
        if el not in alphabet and not el.isdigit() and el != '_':
            print('Неверный символ:', el)
            return
    print('OK')


f()