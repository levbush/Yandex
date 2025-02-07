def add_item(name, cost):
    global receipt
    receipt.append((name, cost))


def print_receipt():
    global n, receipt
    if receipt:
        print(f'Чек {n}. Всего предметов: {len(receipt)}')
        [print(f'{name} - {cost}') for name, cost in receipt]
        print(f'Итого: {sum([el[1] for el in receipt])}')
        print('-----')
        n += 1
        receipt = []


receipt = []
n = 1
