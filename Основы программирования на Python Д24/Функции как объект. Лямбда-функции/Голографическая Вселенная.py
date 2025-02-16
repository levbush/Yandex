def hologram(*args, transformation=1):
    funcs = ['', lambda x: ''.join(
        [x[el].upper() if el == 0 or not x[el - 1].isalpha() else x[el] for el in range(len(x))]),
             lambda x: ''.join(x[el] for el in range(0, len(x), 2)), lambda x: len(x),
             lambda x: ''.join(sorted(list(set(x)))) if len(x) % 2 else x]
    for line in args:
        yield funcs[transformation](line)
