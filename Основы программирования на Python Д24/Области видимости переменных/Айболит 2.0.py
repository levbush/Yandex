def hello(name):
    if None in query:  # type: ignore
        print(f'Здравствуйте, {name}! Подойдите к окошку номер {query.index(None) + 1}')  # type: ignore
        query[query.index(None)] = name  # type: ignore
        return
    print(f'Простите, {name}. Все окна заняты')


def search_card(name):
    if name not in query:  # type: ignore
        print(f'Простите, {name}, дождитесь своей очереди')
        return
    print('Ваша карта не найдена' if name not in base else f'Ваша карта с номером {base.index(name) + 1} найдена')  # type: ignore


def good_bye(name):  # type: ignore
    if name not in query:  # type: ignore
        print(f'Простите, {name}, дождитесь своей очереди')
        return
    print(f'До свидания, не болейте, {name}')
    query[query.index(name)] = None  # type: ignore