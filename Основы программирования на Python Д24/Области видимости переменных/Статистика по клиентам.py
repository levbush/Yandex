data = {}


def get_transactions(t):
    if t == 'print_it':
        for name, amount_n in data.items():
            print(amount_n[1], name, amount_n[0])
        return
    t = t.split('-')[1].split(':')
    data[t[0]] = data.get(t[0], [0, 0])
    data[t[0]][0] += int(t[1])
    data[t[0]][1] += 1