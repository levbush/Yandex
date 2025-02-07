def add_friends(name, friends):
    global data
    if name in data:
        data[name].extend(friends)
    else:
        data[name] = friends


def are_friends(name1, name2):
    return name2 in data[name1]


def print_friends(name):
    print(*sorted(data[name]))


data = {}