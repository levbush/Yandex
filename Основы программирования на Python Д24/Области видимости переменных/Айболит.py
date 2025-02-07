def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')


def search_card(name):
    print('Ваша карта не найдена' if name not in base else f'Ваша карта с номером {base.index(name) + 1} найдена')  # type: ignore